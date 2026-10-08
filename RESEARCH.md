# User brief and research — 8 October 2026

State: RESEARCHED → BUILDING.

User: Site owners reviewing crawler route access before deployment.

Painful task: A broad disallow, group change or wildcard can unexpectedly block a published route; a line-linked batch expectation gate makes the regression visible.

Smallest useful capability: Offline route-case gate with exact-agent/wildcard group selection, repeated exact-group merge, wildcard/end-anchor matches and winning rule line receipts.

Demand is inferred from the documented workflows and review risks. No verified request for this product, adoption, performance advantage or exhaustive feature gap is claimed. Search and repository/README/code/issue reads occurred on 8 October 2026; current exact stars and last-push timestamps below are observations, not quality scores.

Queries: `robots.txt parser sort:stars; robotstxt in:name sort:stars`. Live GitHub search used `sort:stars`. Broad queries return unrelated repository/readme matches; irrelevant results were excluded. Coverage is limited, not an exhaustive global ranking. The highest-star relevant comparable among those examined is [google/robotstxt](https://github.com/google/robotstxt) at 3474 stars.

| Comparable | Stars | Last push (UTC) | License | Workflow, setup, capabilities and tradeoffs |
|---|---:|---|---|---|
| [google/robotstxt](https://github.com/google/robotstxt) | 3474 | 2026-04-01T12:46:49Z | Apache-2.0 | C++ parser/matcher with a single-URL binary and reporting metadata. Mature comparable and most-starred relevant matcher found. C++ build setup; our tool is a strict offline multi-route expectation gate. |
| [temoto/robotstxt](https://github.com/temoto/robotstxt) | 288 | 2026-05-25T08:52:49Z | MIT | Go parser with groups and matching, CLI and clear documentation. Open issue #38 requests listing allow/disallow. Our report connects batch expectations to source lines; this is inferred workflow demand, not a request for our product. |
| [scrapy/protego](https://github.com/scrapy/protego) | 94 | 2026-10-01T17:59:50Z | BSD-3-Clause | Python parser implementing RFC matching with documented pip install, examples and benchmarking. Broader parser compatibility; our tool rejects malformed supported input and explicitly limits crawler behavior. |

Reliability/support observations are limited to public docs, latest source and open issue samples; alternatives were not installed or benchmarked in this run. Examples prove our behavior only. No comparative speed, memory, accuracy or time-to-result measurement was made. Licenses are metadata observations; no competitor implementation/prose was reused.

Acceptance: documented clean install; accepted example; meaningful rejected/input-error examples; deterministic JSON reports; core invariants covered by the unit tests; all remote matrix checks must pass on the intended default head before LIVE. The exact scope/non-goals are in README.md.

Discovery path: relevant GitHub topics and a clear README/linked portfolio index. No messages or third-party issue advertising planned, and no organic growth promise.

Portfolio distinction: compared against all 143 existing repository names/descriptions and relevant CSV/HTTP/parser tools. This is not a fork or a variant of an existing launch. The five candidates address spatial delivery, cache deployment intent, CSP inheritance changes, crawler route expectations and cross-export identifier mapping respectively. masklink-audit does not reconcile numeric CSV differences like table-reconcile, transform data or copy a redaction engine. They are separate user tasks, not subdivisions of one product.

## Commit-linked observations

- [google/robotstxt source snapshot](https://github.com/google/robotstxt/tree/22b355ff855419e6a3ff8ff09c0ad7fdb17116f9) — open issue sample: [#87](https://github.com/google/robotstxt/issues/87), [#86](https://github.com/google/robotstxt/issues/86), [#85](https://github.com/google/robotstxt/issues/85).
- [temoto/robotstxt source snapshot](https://github.com/temoto/robotstxt/tree/cadd395bcc35aaa85a924321f9c7b2d5aa66112c) — open issue sample: [#52](https://github.com/temoto/robotstxt/issues/52), [#50](https://github.com/temoto/robotstxt/issues/50), [#46](https://github.com/temoto/robotstxt/issues/46).
- [scrapy/protego source snapshot](https://github.com/scrapy/protego/tree/1e3bf727402ca02b70bf3b16b1ba4c5d2ef3fe4a) — open issue sample: [#98](https://github.com/scrapy/protego/issues/98).

Standards consulted: [GeoJSON RFC 7946](https://www.rfc-editor.org/rfc/rfc7946.html), [HTTP caching RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html), [Robots RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html), [CSP3](https://www.w3.org/TR/CSP3/). Only the relevant standard informs each bounded tool; conformance is not claimed.
