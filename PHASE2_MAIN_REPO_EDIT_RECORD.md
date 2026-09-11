# Phase 2 Main-Repository Edit Record

## Purpose
This record documents changes made in the two upstream implementation repositories used as dependencies/evidence for this DRF Phase 2 submission. The DRF submission repository does **not** claim ownership or write access to those upstream repositories.

## Upstream repository A — `bhiv-svacs-unified-core`
Phase 2 changes represented by commit:

`30a305506b26677190a7d4bd8271543edcd91ad6`

Documented changes:
- Added structured runtime observability/events and metrics.
- Added safe HTTP exception boundary.
- Added secret-safe telemetry error handling.
- Added `/metrics` and runtime participation/discovery observability.
- Restored the existing pipeline's `generate_intelligence` stage adapter.
- Hardened deterministic registry/storage path handling.
- Added/updated Phase 2 runtime tests and E2E verification.
- Preserved the existing Capability Registry `/modules` contract; no registry schema change.

## Upstream repository B — `bhiv-Capability-Registry-Foundation`
Phase 2 changes represented by commit:

`6980ce5721385639e864eb6e082c836f83c625cb`

Documented changes:
- Enforced required module-registration fields.
- Added optional deployment API-key protection using the existing application boundary (`REGISTRY_API_KEY` / `X-Registry-API-Key`).
- Added request IDs and response timing for traceability.
- Added safe HTTP error boundary.
- Extended health output with contract/authentication configuration state.
- Added Phase 2 security/E2E tests and verification.

## Access / submission boundary
The assignee does not currently have write access to these upstream repositories. Therefore:
- Do not claim that the upstream commits were pushed by this submission.
- The commits above are included as implementation references/evidence.
- The DRF package remains the submission artifact.
- No new registry, authority, undocumented API, or parallel contract was introduced.
