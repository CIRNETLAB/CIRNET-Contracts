# @tinihi-labs/contracts

Public netCIRCUIT DTOs, operation metadata, capture-layout constants, precompiled
offline structural/editor/transport validators, catalog projections and fixtures.
Release version 0.1.1 together with the exact Contracts Python artifact set.
Use the immutable release archive and SHA256 recorded in the system manifest.

Use the root exports for DTO types and metadata, `./validators` for transport,
`./validators.editor` and `./validators.structural` for the other full profiles.
The corresponding `.core` entrypoints retain the bounded eager validator sets.
JSON resources use `./data/*.json`, `./schemas/*.json` and `./fixtures/*.json`.
Validators perform no runtime schema compilation or network reference lookup.
Application semantic adapters continue to enforce their established domain rules.
