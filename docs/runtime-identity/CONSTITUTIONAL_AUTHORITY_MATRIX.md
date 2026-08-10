# Constitutional Authority Matrix

## Purpose

This matrix establishes the constitutional authority boundary of each confirmed runtime participant identified in the BHEX Runtime Inventory.

The objective is to prevent overlapping authority and establish one clear owner for each runtime responsibility.

This is an authority-boundary document, not an implementation redesign.

---

# Constitutional Authority Rules

The following rules govern the matrix:

1. Each participant has one primary constitutional identity.
2. A participant may consume information from another participant without owning that participant's authority.
3. Observability does not create execution authority.
4. Registry visibility does not create execution authority.
5. Evidence persistence does not create execution authority.
6. Knowledge contribution does not create governance authority.
7. Runtime execution does not automatically create governance authority.
8. A UI/dashboard does not become the authority merely because it displays or aggregates runtime state.
9. Candidate and unresolved repositories do not receive constitutional authority.
10. Where implementation evidence is insufficient, authority remains explicitly unassigned rather than inferred.

---

# Primary Constitutional Authority Matrix

| Constitutional Responsibility | Primary Participant | Authority Boundary | Supporting Participants |
|---|---|---|---|
| Runtime Execution | SVACS Unified Core | Owns the documented runtime execution infrastructure and execution chain | SHAKTI observes; Bucket persists evidence |
| Runtime State | SVACS Unified Core | Owns documented runtime state handling within its execution chain | SHAKTI observes |
| Runtime Orchestration | SVACS Unified Core | Owns orchestration surfaces demonstrated by its implementation | Canonical Capability Convergence provides capability composition patterns |
| Capability Registration | Capability Registry Foundation | Owns reusable capability/module registration and metadata | Canonical Capability Convergence consumes/uses registry information |
| Capability Composition | Canonical Capability Convergence | Owns its documented reusable capability composition and integration patterns | Capability Registry provides capability metadata |
| Artifact Persistence | BHIV Bucket | Owns persistence of artifacts/evidence handled by the service | SVACS produces runtime artifacts |
| Evidence Integrity | BHIV Bucket | Owns documented artifact integrity/hash-chain/verification mechanisms | SVACS produces evidence |
| Replay Participation | SVACS Unified Core | Owns replay participation demonstrated within its runtime chain | Bucket supports replay-integrity persistence; SHAKTI presents replay information |
| Operational Visibility | SHAKTI | Owns dashboard presentation and operational visibility | Runtime services provide source data |
| Runtime Observability Presentation | SHAKTI | Owns presentation/aggregation of available runtime health and telemetry information | SVACS and other services produce source telemetry |
| Package Certification | MASTERDB Ingestion Certification Service | Owns validation/certification lifecycle for packages handled by the service | MDU/TANTRA integration subject to verified contracts |
| Certified Knowledge Ingestion | MASTERDB Ingestion Certification Service | Owns certification boundary before trusted ingestion | UniGuru consumes knowledge |
| Knowledge Retrieval | UniGuru | Owns deterministic retrieval within its documented knowledge service | MASTERDB provides certified knowledge/data |
| Knowledge Contribution | UniGuru / MASTERDB boundary | Each owns its documented knowledge function; no universal knowledge authority is inferred | Capability Registry records reusable capability metadata |
| Governance | Not assigned by this matrix | Governance is outside the DRF implementation scope | Sovereign/governance participants must be established separately |
| Sovereign Core Authority | Not assigned by this matrix | Assignment identifies Sovereign Core as an integration dependency, not an implementation owned by DRF | Rajaryan / Sovereign Core |
| Validation & Certification Oversight | Not assigned by this matrix | Vinayak Tiwari is identified by the assignment as Validation & Certification integration | Relevant certification/runtime services |
| TMS Authority | Not assigned | TMS is an assignment-level constitutional dependency; implementation authority requires direct evidence | Runtime participants as contractually applicable |
| GC Authority | Not assigned | GC is an assignment-level constitutional dependency; implementation authority requires direct evidence | Runtime participants as contractually applicable |
| MDU Authority | Not assigned | MDU is an assignment-level constitutional dependency; implementation authority requires direct evidence | MASTERDB certification boundary |

---

# Participant Authority Matrix

## SHAKTI

| Authority Area | Status |
|---|---|
| Dashboard presentation | **OWNED** |
| Operational visibility | **OWNED** |
| Local dashboard resilience | **OWNED** |
| Service-facing read aggregation | **OWNED** |
| Runtime execution | NOT OWNED |
| Runtime orchestration | NOT OWNED |
| Global telemetry authority | NOT OWNED |
| Artifact storage | NOT OWNED |
| Capability registration | NOT OWNED |
| Governance | NOT OWNED |
| Security-token issuance | NOT OWNED |

### Boundary

SHAKTI is an operational visibility and presentation participant.

It consumes runtime/service information but does not become the constitutional owner of those services.

---

# Capability Registry Foundation

| Authority Area | Status |
|---|---|
| Capability registration | **OWNED** |
| Capability metadata | **OWNED** |
| Capability metadata validation | **OWNED** |
| Capability search/filtering | **OWNED** |
| Version metadata | **OWNED** |
| Duplicate prevention | **OWNED** |
| Runtime execution | NOT OWNED |
| Runtime orchestration | NOT OWNED |
| Replay execution | NOT OWNED |
| Governance | NOT OWNED |
| Sovereign authority | NOT OWNED |

### Boundary

The Capability Registry is authoritative for capability registration and metadata.

It is not authoritative for executing registered capabilities.

---

# Canonical Capability Convergence

| Authority Area | Status |
|---|---|
| Canonical capability contract patterns | **OWNED** |
| Capability composition patterns | **OWNED** |
| Capability lifecycle conventions | **OWNED** |
| Capability dependency registration patterns | **OWNED** |
| Capability integration conventions | **OWNED** |
| Universal runtime execution | NOT OWNED |
| Sovereign authority | NOT OWNED |
| Capability Registry ownership | NOT OWNED |
| Global replay authority | NOT OWNED |
| Governance | NOT OWNED |

### Boundary

Canonical Capability Convergence defines reusable capability integration/composition patterns.

It does not become the execution authority for every capability participating in those patterns.

---

# SVACS Unified Core

| Authority Area | Status |
|---|---|
| Documented runtime execution chain | **OWNED** |
| Runtime state handling | **OWNED** |
| Runtime orchestration surfaces | **OWNED** |
| Runtime replay participation | **OWNED** |
| Runtime proof generation | **OWNED** |
| Runtime provenance for its own chain | **OWNED** |
| Runtime telemetry for its own execution path | **OWNED** |
| Runtime validation surfaces | **OWNED** |
| Capability Registry governance | NOT OWNED |
| Sovereign governance | NOT OWNED |
| Global knowledge authority | NOT OWNED |
| Repository governance | NOT OWNED |
| Review governance | NOT OWNED |
| Unrelated application-domain decisions | NOT OWNED |

### Boundary

SVACS Unified Core is the primary runtime execution infrastructure evidenced by the inspected repository.

Its runtime execution authority does not imply sovereign or governance authority.

---

# BHIV Bucket

| Authority Area | Status |
|---|---|
| Artifact persistence | **OWNED** |
| Evidence storage | **OWNED** |
| Artifact retrieval | **OWNED** |
| Storage health | **OWNED** |
| Documented integrity mechanisms | **OWNED** |
| Documented hash-chain mechanisms | **OWNED** |
| Replay-integrity support | **OWNED** |
| Runtime execution | NOT OWNED |
| Runtime orchestration | NOT OWNED |
| Business decisions | NOT OWNED |
| Governance | NOT OWNED |
| Capability registration | NOT OWNED |
| Approval authority | NOT OWNED |

### Boundary

Bucket is an evidence/artifact persistence participant.

It preserves and verifies artifacts; it does not determine runtime execution.

---

# MASTERDB Ingestion Certification Service

| Authority Area | Status |
|---|---|
| Package validation | **OWNED** |
| Certification state transitions | **OWNED** |
| Certification lifecycle | **OWNED** |
| Package registry/lifecycle | **OWNED** |
| Certification provenance | **OWNED** |
| Knowledge-object registration where implemented | **OWNED** |
| Retrieval-readiness state | **OWNED** |
| Certification audit/replay reporting | **OWNED** |
| General runtime execution | NOT OWNED |
| Runtime orchestration | NOT OWNED |
| Sovereign authority | NOT OWNED |
| General capability registration | NOT OWNED |
| Governance | NOT OWNED |

### Boundary

MASTERDB certification is authoritative for the certification boundary of packages it handles.

It does not become a general runtime execution authority.

---

# UniGuru

| Authority Area | Status |
|---|---|
| Deterministic knowledge retrieval | **OWNED** |
| Knowledge corpus mapping | **OWNED** |
| Knowledge-query processing within its interface | **OWNED** |
| Knowledge identifiers/schema handling within its service | **OWNED** |
| Knowledge contribution surfaces | **OWNED** |
| Runtime execution | NOT OWNED |
| Runtime orchestration | NOT OWNED |
| Capability Registry governance | NOT OWNED |
| Sovereign authority | NOT OWNED |
| Runtime replay authority | NOT OWNED |
| Governance | NOT OWNED |

### Boundary

UniGuru is a knowledge-serving participant.

Its knowledge authority is limited to the knowledge service and corpus documented by its implementation.

---

# Authority Ownership Summary

```text
                    CONSTITUTIONAL AUTHORITY

Capability Identity
        │
        ▼
Capability Registry Foundation
        │
        │ registered capability metadata
        ▼
Canonical Capability Convergence
        │
        │ reusable capability composition
        ▼
SVACS Unified Core
        │
        ├──────────────► Runtime State
        │
        ├──────────────► Runtime Orchestration
        │
        ├──────────────► Replay Participation
        │
        ├──────────────► Runtime Proof
        │
        └──────────────► Runtime Telemetry
                              │
                              ▼
                         SHAKTI
                    Operational Visibility
                              │
                              ▼
                           Operator


SVACS Runtime Evidence
        │
        ▼
     BHIV Bucket
 Evidence / Artifacts
        │
        ▼
 Integrity / Verification


Data Package
        │
        ▼
MASTERDB Certification
        │
        ▼
Certified Knowledge
        │
        ▼
     UniGuru
Knowledge Retrieval