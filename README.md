# netCIRCUIT Contracts

Standalone migration candidate **1.0.1**, extracted from Remote revision
`295797c`. The Python distribution is `netcircuit-contracts`; its import
namespace remains `contracts`. The browser package is `@tinihi-labs/contracts`.
Schemas, revisions, protocol versions, frozen wire anchors and public operation
semantics retain their existing meaning. This candidate is not a published
release and does not establish package-registry access or physical support.

Python runtime requires 3.11+. Generator CI uses Python 3.12 and Node 22.
For reproducible CI/release verification, install the complete `requirements-build.lock` with `pip --require-hashes` from a reviewed wheelhouse; `requirements-runtime.lock` independently pins the full runtime closure for Python 3.11/3.12 on Windows AMD64 and Linux x86_64. Install `tools/artifact-paths` with `--no-index --no-build-isolation --no-deps` after the locked build tools. The standalone workflow records the exact offline commands. Then run `npm ci --no-audit --no-fund` in
`packages/public-sdk`. Generation needs no Interface, API, Simulator or Hardware
checkout:

```sh
python -m contracts.codegen.generate_contracts
python -m contracts.codegen.generate_contracts --check
python -m contracts.codegen.sync_editor_catalog --check
python -m contracts.codegen.sync_breadboard_topologies --check
python scripts/check_public_compatibility.py
python -m pytest
node packages/public-sdk/scripts/build.mjs
python -m build --no-isolation --wheel --sdist --outdir /absolute/external/artifacts
```

Before verification, allocate a session through the separately versioned shared
allocator and set `TMP`, `TEMP`, pytest `--basetemp`, logs, npm pack destination
and npm cache to owned external children. Diagnostics never belong in a source
checkout. `scripts/check_public_sdk.mjs --output /absolute/external/owned-child`
inspects the actual npm tarball and executes its extracted runtime without
generator dependencies. It does not publish anything. Bootstrap
`@tinihi-labs/artifact-paths@1.0.0-m1.0` as a separate dev artifact before this
gate, or point `NETCIRCUIT_ARTIFACT_PATHS_MODULE` at that installed package's
absolute module file URL. Outside a Git checkout, supply the shared allocator's
explicit `NETCIRCUIT_ARTIFACTS_CONTEXT` owner/rootset. The gate delegates output
validation to that implementation before creating files; it has no separate
path-validation algorithm and adds no allocator dependency to the core wheel.

`contracts/browser/generated` holds prebuilt DTOs, full/core offline Ajv
validators, operations and capture-layout constants. `contracts/browser/data`
holds the existing public browser catalog projections; `contracts/browser/types`
holds the retained lab compatibility facade. The explicit
`contracts/browser/artifacts.json` maps legacy Remote/Web snapshot paths to
installed package resources. `contracts.resources.generated_artifacts()` reads
those resources without importing or searching for a consumer implementation.
`contracts.codegen.generate_contracts.export_artifacts()` compares/exports that
immutable handoff. Consumers must not regenerate it from retained source.

The npm tarball includes only built public resources under `dist`. Public schema
bundles use the registry's public-reference closure; public profile overrides
and named fixture cases exclude internal identities. Raw mixed-visibility schema
documents, RPC/proto files, canonical device inputs and compatibility baselines
remain available to Python and are absent from npm. The package's validators
enforce canonical schema/profile constraints. Existing Interface semantic
adapters (`parseLab`, document normalization, electrical and capture rules)
remain consumer behavior and must retain their existing conformance tests.

In the source repository, `device-library/**` is the only editable catalog
authority. Generation prepares its `contracts/catalog-source/**` package mirror
and all catalog projections together; check mode detects canonical edits even
when an old packaged mirror still exists. Installed wheels read the immutable
package mirror because they contain no source Device Library directory. Do not
edit that generated mirror as a second catalog authority.

FastAPI registrations in Remote remain the operation authority.
`contracts/api/openapi.json` is the reviewed frozen handoff input, never an
independently editable route model. Generate prerelease schema packages, export
OpenAPI from Remote on that candidate, review/freeze the document, build final
artifacts, then require Remote re-export on the exact final wheel to equal the
frozen bytes. Python/npm distribution version 1.0.1 does not change OpenAPI
application-info version, schema versions, Hardware RPC or NCAP versions.

`contracts/fingerprints.json` records separate canonical-source/public-schema/
OpenAPI fingerprints. Release artifact digests are recorded externally by the
integration handoff; Python and npm artifacts have different contents.

Pure contract assertions are retained under `tests/contracts`. Consumer and
Remote workflow assertions are preserved under `migration/consumer-tests`, with
the exact split in `migration/test-ownership.json`; that handoff directory is not
part of the standalone test suite. No assertion was converted into an automatic
pass to satisfy extraction.
