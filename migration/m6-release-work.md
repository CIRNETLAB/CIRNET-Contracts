# M6 product version and independent generation work

Date: 2026-10-27. Product release target: 0.1.1. This record is separate from historical M1 evidence.

Python metadata, public SDK metadata/lock and installed-wheel exact-version assertions now select 0.1.1. DEV tooling retains its independent versions (Python 1.0.0a1; npm 1.0.0-m1.0). Schema, protocol, compatibility baselines and frozen OpenAPI bytes are unchanged. The compatibility resource map retains its legacy path keys; export requires an explicit destination and deterministic generation owns only Contracts package resources.

Targeted source tests: PASS, 2 tests in 0.35 seconds (metadata parity and explicit destination). The explicit-destination regression failed on the prior signature before the fix. No release artifact or full installed-artifact acceptance is claimed by this targeted check. The migration owner must build from a committed revision, re-export OpenAPI from Remote on the exact final wheel, run standalone generation/resources/public closure and fresh installation, and record actual immutable asset URLs/SHA256.

Build/verify entrypoints: the commands in README.md and .github/workflows/contracts.yml. Use an allocator-owned external environment/output, locked third-party closure and an external CWD for scripts/probe_installed_contracts.py. Historical artifacts and reports remain preserved; no stage/commit/push was performed by this work unit.

The independent clean export exposed checkout-newline drift. Generated browser handoff fixtures now normalize CRLF to LF while canonical fixture/baseline bytes stay unchanged. Explicit LF attributes cover only the generated `contracts/boundary/capture_layout.py` and `contracts/fingerprints.json`, whose current bytes were normalized to LF. A new regression copies canonical inputs externally, generates once with LF and again with CRLF fixture bytes, and compares the entire output inventory. It failed before the fix (38.19 seconds) and passed after it (34.04 seconds). This proves generation byte invariance for that checkout conversion; full clean-export release acceptance remains the migration owner's gate.
