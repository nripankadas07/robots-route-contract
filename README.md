# robots-route-contract

Offline route-case gate with exact-agent/wildcard group selection, repeated exact-group merge, wildcard/end-anchor matches and winning rule line receipts.

For site owners reviewing crawler route access before deployment. A broad disallow, group change or wildcard can unexpectedly block a published route; a line-linked batch expectation gate makes the regression visible.

## Install and first useful result

Python 3.10+; no runtime dependencies, accounts, API keys or network requests from the tool.
Installation may download setuptools from PyPI. No package has been published to a registry.

```sh
git clone https://github.com/nripankadas07/robots-route-contract.git
cd robots-route-contract
python -m venv .venv
# POSIX; Windows: .venv\Scripts\activate
. .venv/bin/activate
python -m pip install .
robots-route-contract robots.txt cases.json
```

The included fixtures are synthetic. `python demo.py` prints the same real example.
CLI exit codes: 0 = accepted/unchanged, 1 = findings/changed, 2 = invalid input or read failure.
Reports are JSON. Input contracts are explicit; see the included JSON files for their schemas.
Use `--help` for arguments. Paths are local and UTF-8. The tool never writes input/output data.

## Check the implementation

```sh
python verify.py
```

Runs 15 meaningful unit checks, Python compilation, then installs this package into a
new virtual environment and exercises accepted, findings and invalid-input CLI cases outside
the source directory. CI repeats this on Python 3.10, 3.12 and 3.14.

## Limits

Strict offline subset, not a crawler or complete RFC 9309 implementation. Takes an exact product token (ASCII letters, underscore, hyphen), not a full User-Agent string. Fetching, redirects, HTTP errors, caching, crawl-delay and typo recovery are unsupported. Unknown directives are reported and ignored; malformed supported lines fail. Route inputs must be path-and-query, without fragments; percent escapes must be valid. Snapshot limit 500 KiB; regex matching and whole-file memory use are not hardened for hostile workloads. No access-control guarantee.

See [RESEARCH.md](RESEARCH.md) for the user brief, dated alternatives and tradeoffs;
[VALIDATION.md](VALIDATION.md) for observed check coverage and
[SUPPORT.md](SUPPORT.md) for contribution/security reporting. MIT licensed;
original implementation using the Python standard library, with no competitor code or prose copied.
