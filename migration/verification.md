# M1 standalone Contracts verification

Recorded 2026-10-24, Asia/Saigon. Status: LOCAL_IMPLEMENTATION_VERIFIED / READY_FOR_REVIEW. No stage, authored source/target commit, merge, push, publication, deployment or M2 was performed.

- Source base: `295797c581acc3935f5e128fd3d23674c728ca65`; target base: `a5b17b1c17bce6a1d097c263110b82e8a4602024`.
- Approved local target branch: `codex/m1-contracts-extract`. Source uses `codex/m1-contracts-consumer`.
- Actual standalone source suite: **498 PASS** in 138.56 s. Separate CI Node allocator bootstrap test: **1 PASS**.
- Final Python wheel1.0.1 SHA256: `ab865f991950fb575d86d3b6bb23646864c706b64c3d0305ba4b9ca9d0237c79`.
- Final source distribution SHA256: `d527113fcd9d41d192576b49b69bf7a7af2f329b61a696c96220b1cf10af1473`.
- Actual public npm1.0.1 tarball SHA256: `17cac7b7ec725581b2ff02078900d5a08ac0f5504df2e1fc3c3703a594c86579`.
- DEV Python1.0.0a1 wheel SHA256: `ff76532c69b2115338edb641660c966c5459dd40cb806f52a1e2e8c379c70a1f`; canonical Node SHA256 `7c42c4fd171ed861b365f08501f3c765282d6bba2dcd6430c9677cddd1abe345`.
- Fresh actual Windows Python3.11/3.12 offline hash-locked installs PASS: resource/catalog/RPC/offline registry/numeric/omission/public closure, all28 projection hashes, exact operations and pipcheck. Finalsdist rebuilt offline:159 package payloads byte-identical to finalwheel, then a separate fresh3.12 runtime probe and pipcheck PASS.
- Runtime/build locks contain12/40 packages and65 reviewed wheel hashes. Four CPython/platform wheel-tag closures PASS offline (WindowsAMD64/Linuxx86_64 x3.11/3.12). Linux execution and hosted Actions are NOT_RUN. Valid-wheel tampering was accepted by prior unhashed installation and rejected before installation under the new hash locks.
- Allocator Node15/Python2 cases PASS, including Git families, aliases, denied discovery, unlisted Git destinations and inherited ownership/cleanup.
- Final Remote consumer suite: **1313 PASS /4 SKIP** in471.71s. Separate installer3PASS group includes one transition case added after full collection. Skips: two Windows file-symlink privileges and two optionalFPGA tools. Existing deprecation warning only. Exact selected154 package files, OpenAPI re-export, compatibility, actualSDK public88baseline/89profile cases and assembled four-wheel installation/migration/CLI/simulation checks PASS.
- Web1435PASS; build/type/boundary checks PASS; two relevant real Chromium156.0.8078.4 login and API/RPC/AND simulation/capture/history browser cases PASS. No screenshots were produced/visually inspected.
- Independent read-only review findings repaired: CI allocator module loading, same-version exactwheel replacement, output alias/repeat-write handling, full dependency hash locks.

Canonical build and ownership commands: [README](../README.md). FastAPI operation export remains Remote-owned; this repository consumes its reviewed frozen OpenAPI snapshot. Device Library source is the only editable catalog owner; installed wheels use the packaged mirror. Wire/schema/protocol versions and public baselines were preserved. Original target working LICENSE bytes were preserved; sdist uses the exact Git LF license content.

[History provenance](history-provenance.md) records197 exactselectedblobs,43retainedcommit mappings, author/committer identity/timestamps, fsck and realbundle restoration. Extracted ancestry is in a verified durable bundle and is not yet connected to target: a connecting merge/commit needs separate authorization. Committing this current snapshot alone does not connect that history.

The six unpublished local artifacts and manifest are retained outside diagnostic sessions under `C:/Users/trann/.codex/visualizations/2026/10/24/01a16c1e-02ba-7253-9226-6f4a43582df4/migration-release-artifacts/m1-contracts-1.0.1-20261024-LiyD0Y/`. Verified history bundles are retained under the sibling `migration-history-source-archives/m1-contracts-20261024-LiyD0Y/` directory. They are not hosted releases.

Pending separate authorization: ancestry integration, immutable artifact publication and authenticated private consumer ACL/hostedCI proof. Retained Remote source is not deleted. Rollback preserves both working diffs and restores M1-owned source/consumer manifests/tooling together to recorded bases in a recreated environment; retain pre-existing M0 Markdown, data, historical evidence and source archives. Do not pair the strict1.0.1 forwarding shim with1.0.0. No reset/clean or destructive rollback has been executed.

Temporary raw evidence is inspected and cleaned by the parent through each session's original allocator ownership context. Durable artifact/source archives remain. Detailed integration evidence is handed off in Remote at `docs/verification/2026-10-24-multi-repo-migration-m1.md`.

Remote output-policy exception: default pytest caching wrote ignored diagnostics to its root/API cache trees during verification. Those trees are preserved, and the detailed Remote report discloses the initial violation. Root/API/Simulator/Hardware configs now disable cacheprovider; four real project subprocess regressions pass with source cache bytes/mtime unchanged. Standalone Contracts already disabled this plugin. No source cache deletion or relocation was performed.

Cleanup confirmed: owned external sessions LiyD0Y and iUF6uQ were removed through the shared allocator after process exit and evidence inspection. Durable six release artifacts/manifest and three verified source/history bundles remain outside those sessions. Original source/target HEADs and empty indexes are unchanged. Source caches are preserved under the explicitly recorded policy exception.
