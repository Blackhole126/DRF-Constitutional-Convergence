# Runtime Identity Cards

## Purpose

This document establishes the permanent constitutional identity of each runtime participant identified through the current BHEX evidence inventory.

The objective is to ensure that every confirmed runtime participant has exactly one primary constitutional identity and that its authority boundary does not overlap with another participant.

A participant may consume services from, publish evidence to, or integrate with multiple constitutional layers. Such integration does not create additional authority.

---

# Constitutional Identity Rule

Each confirmed runtime participant receives exactly one primary constitutional identity.

The following rules apply:

1. One participant = one primary constitutional identity.
2. Integration with another layer does not transfer constitutional ownership.
3. Observability does not create execution authority.
4. Registry participation does not create execution authority.
5. Evidence storage does not create governance authority.
6. Knowledge contribution does not create runtime orchestration authority.
7. Candidate or unresolved repositories do not receive permanent constitutional identities until sufficient evidence exists.
8. Authority must be explicitly stated both positively and negatively.

---

# Confirmed Runtime Participants

## 1. SHAKTI — Operational Runtime Visibility Participant

### Constitutional Layer
Operational / Observability Surface

### Permanent Identity
**SHAKTI Executive Dashboard Capability**

### Purpose
Provide configuration-driven operational visibility across runtime health, telemetry, replay, evidence, workflow and registry-facing operational surfaces.

### Owner
BHEX project owner/team.

The supplied repository evidence does not establish a single named constitutional owner.

### Runtime Position
Downstream observational and operational-consumption surface over multiple backend/runtime services.

SHAKTI does not become the authority of the backend services that it observes.

### Authority Owned

- Dashboard presentation
- Operational visibility
- Runtime-health presentation
- Service-facing read aggregation
- Local UI resilience
- Configuration-driven dashboard composition
- Presentation of replay/evidence/registry information available through its configured services

### Authority Explicitly NOT Owned

- Runtime execution authority
- Global orchestration authority
- Sovereign Core authority
- Global telemetry ownership
- Artifact persistence authority
- Capability registry ownership
- Security-token issuance
- Governance decisions

### Evidence Basis

The SHAKTI repository describes the application as a standalone frontend/passive consumer of multiple backend services. Its architecture follows a primitive → layout → dashboard model and provides operational surfaces for runtime health, replay, evidence, registries and telemetry.

### Constitutional Boundary

**SHAKTI observes and presents runtime state; it does not become the runtime authority merely because it displays that state.**

---

# 2. Capability Registry Foundation — Capability Registry Participant

### Constitutional Layer
Registry / Capability Layer

### Permanent Identity
**Capability Registry Foundation**

### Purpose
Maintain the source of truth for reusable software capability/module metadata, categories, versions and registration information.

### Owner
BHEX project owner/team.

The supplied repository evidence does not establish a single named constitutional owner.

### Runtime Position
Registry service positioned beside runtime participants and consumed by capabilities and ecosystem tooling requiring capability metadata.

### Authority Owned

- Capability/module registration
- Capability metadata
- Metadata validation
- Category management
- Version metadata
- Capability search/filtering
- Duplicate prevention
- Registry API surface

### Authority Explicitly NOT Owned

- Runtime execution
- Runtime orchestration
- AI workflow execution
- Replay execution
- Governance decisions
- Sovereign Core authority
- Application-domain execution decisions

### Evidence Basis

The repository describes itself as a single source of truth for reusable software modules and provides REST-based registration, metadata, validation, versioning and search functionality.

The repository documentation explicitly distinguishes capability registration from runtime execution and orchestration.

### Constitutional Boundary

**The Capability Registry records and exposes capability identity; it does not execute the capability.**

---

# 3. Canonical Capability Convergence — Capability Composition Participant

### Constitutional Layer
Capability / Composition Layer

### Permanent Identity
**Canonical Capability Convergence**

### Purpose
Provide standardized capability contracts and reusable capability-composition patterns that allow capabilities to be integrated into the wider ecosystem without creating parallel architectures.

### Owner
BHEX project owner/team.

The supplied repository evidence does not establish a single named constitutional owner.

### Runtime Position
Capability integration and composition layer adjacent to the Capability Registry and runtime participants.

### Authority Owned

- Canonical capability contract patterns
- Capability composition rules implemented by the project
- Capability lifecycle conventions
- Capability dependency registration patterns
- Capability integration patterns
- Capability health/integration conventions defined by the project

### Authority Explicitly NOT Owned

- Sovereign Core authority
- Universal runtime execution authority
- Runtime orchestration authority outside its own documented composition capability
- Capability Registry ownership
- Governance authority
- Repository governance
- Global replay authority

### Evidence Basis

Repository documentation describes reusable capability design, standardized capability contracts, plug-and-play integration, lifecycle management, dependency registration and integration readiness with the wider TANTRA/BHIV ecosystem.

### Constitutional Boundary

**Canonical Capability Convergence defines how reusable capabilities converge into the ecosystem; it does not become the execution authority for every capability it helps compose.**

---

# 4. SVACS Unified Core — Runtime Execution Infrastructure Participant

### Constitutional Layer
Runtime Reference / Execution Infrastructure

### Permanent Identity
**SVACS Unified Core Runtime**

### Purpose
Provide the documented runtime execution chain together with state handling, orchestration, replay, provenance, telemetry, validation and runtime-proof surfaces.

### Owner
BHEX project owner/team.

Repository contributors and component responsibilities may be documented within the repository, but the supplied evidence does not establish one named constitutional owner for every runtime component.

### Runtime Position
Core runtime execution infrastructure positioned between higher-level constitutional authorities and supporting replay, evidence, persistence and observability infrastructure.

### Authority Owned

- Its documented runtime execution chain
- Runtime state handling
- Runtime orchestration surfaces implemented by the core
- Runtime replay participation
- Runtime proof generation
- Runtime provenance handling for its own chain
- Runtime telemetry for its own execution path
- Runtime validation surfaces

### Authority Explicitly NOT Owned

- Sovereign Core governance
- Global governance decisions
- Universal capability registration
- Global knowledge authority
- Repository governance
- Review governance
- Unrelated application/domain decisions
- Security authority outside documented runtime contracts

### Evidence Basis

The repository contains runtime contracts, core executor components, orchestration, state handling, replay, runtime proof, provenance, telemetry and validation surfaces.

The repository's runtime evidence demonstrates a chain involving runtime execution, state, storage/evidence, replay, observability and dashboard surfaces.

### Constitutional Boundary

**SVACS Unified Core owns the runtime execution infrastructure evidenced by its implementation; it does not become sovereign governance merely because it executes runtime operations.**

---

# 5. BHIV Bucket — Evidence and Artifact Persistence Participant

### Constitutional Layer
Evidence / Persistence Infrastructure

### Permanent Identity
**BHIV Bucket Evidence and Artifact Store**

### Purpose
Provide persistent artifact/evidence storage and integrity mechanisms required by runtime participants for durable evidence, verification and replay-integrity workflows.

### Owner
BHEX project owner/team.

The supplied repository evidence does not establish a single named constitutional owner.

### Runtime Position
Supporting infrastructure below runtime execution and adjacent to replay, evidence and observability participants.

### Authority Owned

- Artifact persistence
- Evidence/artifact retrieval
- Storage health
- Append-oriented evidence persistence where implemented
- Integrity verification mechanisms implemented by the service
- Hash-chain/integrity support where implemented
- Replay-integrity support where implemented

### Authority Explicitly NOT Owned

- Runtime execution
- Runtime orchestration
- Business decisions
- Governance decisions
- Capability registration
- Sovereign Core authority
- Knowledge governance
- Approval authority

### Evidence Basis

The repository provides artifact/evidence storage functionality, health surfaces, integrity mechanisms and replay-integrity/verification material.

### Constitutional Boundary

**Bucket preserves and verifies runtime artifacts/evidence; it does not decide what the runtime should execute.**

---

# 6. MASTERDB Ingestion Certification Service — Certification and Knowledge Ingestion Participant

### Constitutional Layer
Validation / Knowledge Ingestion

### Permanent Identity
**MASTERDB Ingestion Certification Service**

### Purpose
Validate, certify and lifecycle-manage data packages before trusted MASTERDB ingestion.

### Owner
BHEX project owner/team.

The supplied repository evidence does not establish a single named constitutional owner.

### Runtime Position
Validation and certification boundary upstream of trusted knowledge/data ingestion and downstream of data/package producers.

### Authority Owned

- Package validation
- Certification state transitions
- Package registry/lifecycle
- Provenance records for certified packages
- Knowledge-object registration where implemented
- Retrieval-readiness status
- Audit/replay reporting for its certified packages
- Certification evidence

### Authority Explicitly NOT Owned

- General runtime execution
- Runtime orchestration
- Sovereign Core authority
- General capability registration
- Global governance decisions
- Unrelated application-domain decisions

### Evidence Basis

Repository documentation describes deterministic certification states and service surfaces for validation, certification, registry, knowledge objects, retrieval, audit/replay, MDU compatibility and TANTRA-oriented data registration.

### Constitutional Boundary

**MASTERDB certification determines whether a data package satisfies the documented certification boundary; it does not become the runtime execution authority.**

---

# 7. UniGuru — Knowledge Retrieval Participant

### Constitutional Layer
Knowledge / Knowledge Contribution

### Permanent Identity
**UniGuru Knowledge Retrieval Runtime**

### Purpose
Provide deterministic knowledge retrieval and mapping over its documented knowledge corpus and contribute reusable knowledge structures to the broader ecosystem.

### Owner
BHEX project owner/team.

The supplied repository evidence does not establish a single named constitutional owner.

### Runtime Position
Knowledge-serving participant downstream of certified knowledge/data and upstream of consumers requiring deterministic knowledge retrieval.

### Authority Owned

- Deterministic knowledge retrieval
- Knowledge corpus mapping
- Knowledge-query processing within its documented interface
- Knowledge identifiers/schema handling within its own service
- Knowledge contribution surfaces implemented by the project

### Authority Explicitly NOT Owned

- Runtime execution
- Runtime orchestration
- Capability Registry governance
- Sovereign Core authority
- Governance decisions
- Runtime replay authority
- Repository governance

### Evidence Basis

Repository documentation describes a decoupled deterministic retrieval/RAG architecture, Kosha-oriented data structures, knowledge identifiers and knowledge-graph/data surfaces.

### Constitutional Boundary

**UniGuru serves knowledge; it does not become the authority for the runtime that consumes that knowledge.**

---

# Candidate Participants

## PARIKSHAN — Validation Candidate

### Status

**Candidate — no permanent constitutional identity assigned yet.**

### Reason

The BHEX repository is present and exposes backend/frontend structure, but the currently available public repository evidence is insufficient to establish the exact runtime responsibility, authority boundary, contracts and permanent constitutional home.

### Current Rule

PARIKSHAN must **not** be treated as a confirmed constitutional runtime participant until its implementation and validation role are directly evidenced.

### Prohibited Assumption

Do not infer execution, certification, review, governance or registry authority solely from the repository name.

---

# Unresolved Repositories

The following repositories remain outside the permanent identity-card set until sufficient implementation evidence is inspected:

- `bhiv-QCG`
- `bhiv-workflow-blackhole`
- `bhiv-pravah`
- `bhiv-Ai-Artha`
- `bhiv-KESHAV-4`
- `bhiv-NYAI`
- `bhiv-News-Ai`
- `bhiv-Mitra`
- `bhiv-ai-crm`
- `BHIV-Design-Engine-`
- `BHIV-ttg`
- `bhiv-AI-Content`
- `bhiv-Infiverse-HR`
- `svacs-demo`
- `bhiv-intelligence-tenderAI`
- `bhiv-Composition-Workspace-And-Coordination-Console`
- `bhiv-Nagar-Pranali`
- `bhiv-Pradnya`
- `bhiv-Namami-Gange`
- `bhiv-biometric-blackhole`
- `blackhole_auth`
- `bhiv-prompt-runner01`
- `BHIV-Agent-Platform`
- `bhiv-gurukul-assesment`

No constitutional authority is assigned to these repositories by this document.

---

# Excluded Repository

## bhiv-Trade_Bot_

The repository is private and is therefore excluded from the current public BHEX evidence set.

No private implementation details are used to assign DRF constitutional authority.

---

# Identity Non-Overlap Matrix

| Participant | Primary Identity | Execution | Registry | Evidence | Observability | Knowledge |
|---|---|---:|---:|---:|---:|---:|
| SHAKTI | Operational Runtime Visibility | No | View/consume | View | Presentation | No |
| Capability Registry Foundation | Capability Registry | No | **Owns capability registry** | No | Registry health | Metadata only |
| Canonical Capability Convergence | Capability Composition | No universal execution | Capability integration | No | Integration health | No |
| SVACS Unified Core | Runtime Execution Infrastructure | **Owns documented runtime execution** | Consume | Produce/participate | Produce/consume | No |
| BHIV Bucket | Evidence & Artifact Persistence | No | No | **Owns artifact persistence/integrity** | Storage health | No |
| MASTERDB Certification | Certification & Knowledge Ingestion | No | Package certification registry | Certification evidence | Service health | **Certified knowledge/data** |
| UniGuru | Knowledge Retrieval | No | No | Knowledge retrieval evidence | Service health | **Knowledge retrieval** |

---

# Constitutional Separation Principle

The identities above are deliberately separated:

```text
Capability Registry
        │
        │ capability metadata
        ▼
Canonical Capability Convergence
        │
        │ capability integration
        ▼
Runtime Execution Infrastructure
        │
        ├──────────────► Replay
        │
        ├──────────────► Evidence / Bucket
        │
        └──────────────► Observability / SHAKTI
                                     
Certified Knowledge
        │
        ▼
MASTERDB Certification
        │
        ▼
UniGuru / Knowledge Contribution