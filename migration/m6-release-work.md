# M6 product version and independent generation work

Date: 2026-10-27. Product release target: 0.1.1. This record is separate from historical M1 evidence.

Python metadata, public SDK metadata/lock and installed-wheel exact-version assertions now select 0.1.1. DEV tooling retains its independent versions (Python 1.0.0a1; npm 1.0.0-m1.0). Schema, protocol, compatibility baselines and frozen OpenAPI bytes are unchanged. The compatibility resource map retains its legacy path keys; export requires an explicit destination and deterministic generation owns only Contracts package resources.

Targeted source tests: PASS, 2 tests in 0.35 seconds (metadata parity and explicit destination). The explicit-destination regression failed on the prior signature before the fix. No release artifact or full installed-artifact acceptance is claimed by this targeted check. The migration owner must build from a committed revision, re-export OpenAPI from Remote on the exact final wheel, run standalone generation/resources/public closure and fresh installation, and record actual immutable asset URLs/SHA256.

Build/verify entrypoints: the commands in README.md and .github/workflows/contracts.yml. Use an allocator-owned external environment/output, locked third-party closure and an external CWD for scripts/probe_installed_contracts.py. Historical artifacts and reports remain preserved; no stage/commit/push was performed by this work unit.
