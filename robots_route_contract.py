"""Trace offline robots.txt route expectations for an exact product token."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote

UNRESERVED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"


def normalize(text, operators=False):
    if re.search(r"%(?![0-9A-Fa-f]{2})", text):
        raise ValueError("malformed percent escape")
    def pct(m):
        n = int(m[0][1:], 16)
        return chr(n) if chr(n) in UNRESERVED else "%%%02X" % n
    safe = "/%!';():@&=+,?[]~-._" + ("*$" if operators else "")
    return re.sub(r"%[0-9A-Fa-f]{2}", pct, quote(text, safe=safe))


def parse(text):
    if not isinstance(text, str) or len(text.encode("utf-8")) > 512000:
        raise ValueError("UTF-8 robots snapshot must be at most 512000 bytes")
    groups, agents, rules, ignored = [], [], [], []
    for line, raw in enumerate(text.lstrip("\ufeff").splitlines(), 1):
        raw = raw.split("#", 1)[0].strip()
        if not raw:
            continue
        name, sep, value = raw.partition(":")
        if not sep:
            raise ValueError("line %d: colon required" % line)
        name, value = name.strip().lower(), value.strip()
        if name == "user-agent":
            if rules:
                groups.append({"agents": agents, "rules": rules}); agents, rules = [], []
            if value != "*" and not re.fullmatch(r"[A-Za-z_-]+", value):
                raise ValueError("line %d: supported product token required" % line)
            agents.append(value.lower())
        elif name in ("allow", "disallow"):
            if not agents:
                raise ValueError("line %d: rule before user-agent" % line)
            if value and not value.startswith("/"):
                raise ValueError("line %d: route pattern must start with slash" % line)
            pattern = normalize(value, operators=True)
            # Encoded * and $ remain literal escapes, not operators.
            end = pattern.endswith("$")
            body = pattern[:-1] if end else pattern
            regex = "^" + ".*".join(re.escape(x) for x in body.split("*")) + ("$" if end else "")
            specificity = len(re.sub(r"%[0-9A-F]{2}", "x", body.replace("*", "")))
            rules.append({"line": line, "action": name, "pattern": pattern, "specificity": specificity, "regex": regex})
        else:
            ignored.append({"line": line, "directive": name})
    if agents:
        groups.append({"agents": agents, "rules": rules})
    return groups, ignored


def trace(text, agent, path):
    if not isinstance(agent, str) or not re.fullmatch(r"[A-Za-z_-]+", agent):
        raise ValueError("exact ASCII product token required")
    if not isinstance(path, str) or not path.startswith("/") or "#" in path or any(ord(c) < 32 for c in path):
        raise ValueError("path-and-query starting with slash required; no fragment/control characters")
    groups, ignored = parse(text)
    exact = [g for g in groups if agent.lower() in g["agents"]]
    selected = exact or [g for g in groups if "*" in g["agents"]]
    target = normalize(path)
    if target.split("?", 1)[0] == "/robots.txt":
        return {"allowed": True, "group": "implicit robots.txt access", "winning_rule": None,
                "matching_rules": [], "ignored_directives": ignored}
    matched = [r for g in selected for r in g["rules"] if r["pattern"] and re.search(r["regex"], target)]
    best = max(matched, key=lambda r: (r["specificity"], r["action"] == "allow", -r["line"]), default=None)
    public = lambda r: {k: v for k, v in r.items() if k != "regex"}
    return {"allowed": best is None or best["action"] == "allow", "group": "exact" if exact else "wildcard" if selected else "none",
            "winning_rule": public(best) if best else None, "matching_rules": [public(r) for r in matched], "ignored_directives": ignored}


def check(text, cases):
    if not isinstance(cases, list) or not cases:
        raise ValueError("nonempty route-case list required")
    rows = []
    for i, c in enumerate(cases):
        if not isinstance(c, dict) or set(c) != {"agent", "path", "allowed"} or type(c["allowed"]) is not bool:
            raise ValueError("each case requires agent, path, boolean allowed only")
        r = trace(text, c["agent"], c["path"])
        rows.append({"case": i, "expected": c["allowed"], "ok": r["allowed"] == c["allowed"], **r})
    return {"ok": all(r["ok"] for r in rows), "cases": rows}


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("robots"); p.add_argument("cases"); a = p.parse_args()
    try:
        r = check(Path(a.robots).read_text(encoding="utf-8"), json.loads(Path(a.cases).read_text(encoding="utf-8")))
        print(json.dumps(r, sort_keys=True)); return 0 if r["ok"] else 1
    except (ValueError, OSError, RecursionError) as e:
        print(json.dumps({"error": str(e)})); return 2


if __name__ == "__main__":
    raise SystemExit(main())
