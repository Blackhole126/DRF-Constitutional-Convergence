
# BHEX Runtime Participation Map

## 1. Purpose

This document permanently positions the confirmed runtime and supporting participants identified from the BHEX repository population within the TANTRA/BHIV Living Organism.

The objective is to demonstrate where the Runtime Reference Implementation participates constitutionally and how it connects to adjacent runtime, registry, evidence, observability, and knowledge layers.

This document does not redesign the Runtime Reference Implementation, introduce a parallel architecture, or assign authority that is not supported by available repository evidence.

---

# 2. Constitutional Positioning Principle

The Runtime Reference Implementation is positioned as a reusable runtime participant within the wider TANTRA/BHIV ecosystem.

The constitutional positioning supplied by the assignment is:

```text
Sovereign Core
      ↓
    RAJYA
      ↓
    DGIC
      ↓
Runtime Reference Implementation
      ↓
Execution Infrastructure
      ↓
Replay
      ↓
Evidence
      ↓
Observability
      ↓
Knowledge Contribution
````

This represents constitutional positioning and dependency direction.

It does not mean every relationship shown above is necessarily a direct API call.

---

# 3. Sovereign Core

## Constitutional Home

Sovereign / Constitutional Layer

## Assignment Relationship

The assignment identifies:

**Rajaryan — Sovereign Core**

as a primary integration relationship.

## Position

```text
Sovereign Core
      ↓
    RAJYA
```

## Purpose

Sovereign Core represents the constitutional boundary above the runtime ecosystem.

## DRF Authority

DRF does not implement or claim Sovereign Core authority.

## Adjacent Layers

* RAJYA
* DGIC
* Runtime Reference Implementation

## Evidence Boundary

The assignment establishes Sovereign Core as an integration dependency.

DRF does not invent implementation-level APIs, events, schemas, or authority for Sovereign Core without direct repository evidence.

---

# 4. RAJYA

## Constitutional Home

Constitutional Integration Layer

## Position

```text
Sovereign Core
      ↓
    RAJYA
      ↓
    DGIC
```

## Purpose

RAJYA is identified by the assignment as a constitutional layer between Sovereign Core and the runtime ecosystem.

## DRF Authority

DRF does not implement or claim RAJYA authority.

## Adjacent Layers

* Sovereign Core
* DGIC
* Runtime Reference Implementation

## Evidence Boundary

Implementation-level RAJYA contracts are not inferred without direct repository evidence.

---

# 5. DGIC

## Constitutional Home

Constitutional Integration / Control Layer

## Position

```text
RAJYA
  ↓
DGIC
  ↓
Runtime Reference Implementation
```

## Purpose

DGIC is identified by the assignment as the constitutional layer immediately upstream of the Runtime Reference Implementation.

## DRF Authority

DRF does not implement or claim DGIC authority.

## Adjacent Layers

* RAJYA
* Runtime Reference Implementation
* Execution Infrastructure

## Evidence Boundary

Exact DGIC implementation contracts are not invented without direct repository evidence.

---

# 6. Runtime Reference Implementation

## Constitutional Home

Runtime Layer

## Permanent Position

```text
Sovereign Core
      ↓
    RAJYA
      ↓
    DGIC
      ↓
Runtime Reference Implementation
```

## Purpose

The Runtime Reference Implementation is the reusable runtime participant that this DRF assignment is responsible for positioning within the TANTRA/BHIV ecosystem.

## Primary Integration

The assignment identifies:

**Vijay — Runtime Reference Implementation**

as the primary integration relationship.

## Runtime Position

The runtime sits downstream of the constitutional control layers and upstream of the execution, replay, evidence, and observability infrastructure.

## Authority Owned

The Runtime Reference Implementation owns only the runtime responsibilities explicitly demonstrated by its implementation and contracts.

## Authority Not Owned

The Runtime Reference Implementation does not automatically own:

* Sovereign Core authority
* RAJYA authority
* DGIC authority
* Governance
* Capability Registry governance
* Knowledge governance
* Repository governance
* Review governance

---

# 7. Execution Infrastructure

## Constitutional Home

Runtime Execution Infrastructure

## Confirmed BHEX Participant

**SVACS Unified Core**

## Position

```text
Runtime Reference Implementation
            ↓
Execution Infrastructure
            ↓
     SVACS Unified Core
```

## Purpose

Provide the documented runtime execution chain and associated runtime infrastructure.

The inspected repository evidence indicates responsibilities around:

* Runtime execution
* Runtime state
* Orchestration
* Replay
* Provenance
* Telemetry
* Validation
* Runtime proof

## Authority Owned

SVACS Unified Core owns the documented runtime execution infrastructure demonstrated by its implementation.

## Authority Not Owned

It does not automatically own:

* Sovereign governance
* Universal capability registration
* Knowledge governance
* Repository governance
* Review governance
* Unrelated application/domain decisions

## Adjacent Layers

### Upstream

* Runtime Reference Implementation
* DGIC / constitutional integration boundary

### Downstream

* Runtime State
* Replay
* Evidence
* Observability

---

# 8. Runtime State

## Constitutional Home

Runtime Execution Infrastructure

## Primary Participant

SVACS Unified Core

## Position

```text
Runtime Execution
      ↓
Runtime State
      ↓
Replay / Evidence / Observability
```

## Purpose

Maintain runtime state required by the documented runtime execution chain.

## Authority

State authority is limited to the runtime state lifecycle demonstrated by the runtime implementation.

## Authority Not Owned

Runtime state does not automatically become:

* Governance state
* Sovereign state
* Capability Registry state
* Knowledge governance state

---

# 9. Replay

## Constitutional Home

Replay / Runtime Evidence Layer

## Primary Participant

SVACS Unified Core

## Supporting Participant

BHIV Bucket

## Position

```text
Runtime Execution
      ↓
    Replay
      ↓
Evidence / Integrity
```

## Purpose

Provide replay participation for runtime events, execution lineage, and runtime verification where implemented.

## Authority

SVACS Unified Core owns replay participation demonstrated within its runtime chain.

BHIV Bucket provides persistence and integrity support for applicable replay and evidence artifacts.

## Authority Not Owned

Replay does not become:

* Runtime execution authority
* Governance authority
* Capability Registry authority
* Knowledge governance authority

---

# 10. Evidence

## Constitutional Home

Evidence / Artifact Infrastructure

## Primary Participant

BHIV Bucket

## Supporting Participant

SVACS Unified Core

## Position

```text
Runtime Execution
      ↓
Runtime Evidence
      ↓
BHIV Bucket
      ↓
Persistent Artifact / Integrity
```

## Purpose

Preserve runtime artifacts and evidence and provide documented persistence and integrity mechanisms.

## Authority Owned

BHIV Bucket owns artifact persistence and integrity mechanisms implemented by the service.

SVACS Unified Core remains responsible for producing runtime evidence from its own execution chain.

## Authority Not Owned

BHIV Bucket does not decide:

* What executes
* When execution occurs
* Runtime orchestration
* Governance decisions
* Capability registration
* Business decisions

---

# 11. Observability

## Constitutional Home

Operational / Observability Layer

## Primary Participant

SHAKTI

## Supporting Participant

SVACS Unified Core and other services consumed by SHAKTI

## Position

```text
Runtime Services
      ↓
Telemetry / Health
      ↓
SHAKTI
      ↓
Operational Visibility
```

## Purpose

SHAKTI provides operational visibility across runtime health, telemetry, replay, evidence, workflow, and registry-facing surfaces.

The supplied SHAKTI documentation describes it as a standalone frontend SPA and a passive consumer of multiple external services.

## Authority Owned

SHAKTI owns:

* Dashboard presentation
* Operational visibility
* Local UI resilience
* Service-facing read aggregation
* Presentation of runtime health information

## Authority Not Owned

SHAKTI does not own:

* Runtime execution
* Runtime orchestration
* Global telemetry ownership
* Artifact storage
* Capability registration
* Security-token issuance
* Sovereign governance

---

# 12. Capability Registry

## Constitutional Home

Capability Registry Layer

## Primary Participant

Capability Registry Foundation

## Position

```text
Capability Identity
        ↓
Capability Registry
        ↓
Capability Consumers / Composition
```

## Purpose

Provide reusable capability/module metadata, registration, validation, versioning, and search.

## Authority Owned

Capability Registry Foundation owns:

* Capability registration
* Capability metadata
* Metadata validation
* Version metadata
* Search/filtering
* Duplicate prevention where implemented

## Authority Not Owned

Capability Registry Foundation does not own:

* Runtime execution
* Runtime orchestration
* Replay execution
* Sovereign governance

---

# 13. Canonical Capability Convergence

## Constitutional Home

Capability / Composition Layer

## Primary Participant

Canonical Capability Convergence

## Position

```text
Capability Registry
        ↓
Canonical Capability Convergence
        ↓
Runtime Integration
```

## Purpose

Provide reusable capability contracts, composition patterns, lifecycle conventions, and dependency integration.

## Authority Owned

The participant owns its documented capability composition and integration responsibilities.

## Authority Not Owned

It does not automatically own:

* Universal runtime execution
* Sovereign authority
* Capability Registry authority
* Global replay authority
* Governance authority

---

# 14. MASTERDB Certification

## Constitutional Home

Validation / Knowledge Ingestion Layer

## Primary Participant

MASTERDB Ingestion Certification Service

## Position

```text
Data / Knowledge Package
          ↓
MASTERDB Certification
          ↓
Certified Knowledge
```

## Purpose

Validate and certify data packages before trusted knowledge/data ingestion.

## Authority Owned

The certification service owns its documented:

* Package validation
* Certification lifecycle
* Certification states
* Package provenance
* Certification evidence
* Knowledge-object registration where implemented
* Retrieval-readiness state
* Audit/replay reporting where implemented

## Authority Not Owned

It does not automatically own:

* Runtime execution
* Runtime orchestration
* Sovereign authority
* General capability registration
* Governance authority

---

# 15. UniGuru

## Constitutional Home

Knowledge Layer

## Primary Participant

UniGuru

## Position

```text
Certified Knowledge
       ↓
     UniGuru
       ↓
Knowledge Retrieval / Contribution
```

## Purpose

Provide deterministic knowledge retrieval and reusable knowledge contribution.

The supplied repository evidence describes UniGuru as a deterministic knowledge retrieval system using documented knowledge/Kosha structures.

## Authority Owned

UniGuru owns:

* Deterministic knowledge retrieval
* Knowledge corpus mapping
* Knowledge-query processing within its documented interface
* Knowledge contribution surfaces

## Authority Not Owned

UniGuru does not automatically own:

* Runtime execution
* Runtime orchestration
* Capability Registry governance
* Sovereign authority
* Runtime replay authority
* General ecosystem governance

---

# 16. Complete Runtime Participation Map

```text
                         TANTRA / BHIV
                              │
                              ▼
                       ┌─────────────┐
                       │ Sovereign   │
                       │    Core     │
                       └──────┬──────┘
                              │
                              ▼
                       ┌─────────────┐
                       │    RAJYA    │
                       └──────┬──────┘
                              │
                              ▼
                       ┌─────────────┐
                       │    DGIC     │
                       └──────┬──────┘
                              │
                              ▼
                ┌─────────────────────────┐
                │ Runtime Reference       │
                │ Implementation          │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Execution Infrastructure│
                │ SVACS Unified Core      │
                └───────┬───────┬─────────┘
                        │       │
                        │       └──────────────┐
                        │                      │
                        ▼                      ▼
                 ┌────────────┐         ┌────────────┐
                 │   State    │         │   Replay   │
                 └────────────┘         └─────┬──────┘
                                              │
                                              ▼
                                       ┌─────────────┐
                                       │   Evidence  │
                                       │ BHIV Bucket │
                                       └──────┬──────┘
                                              │
                                              ▼
                                       ┌─────────────┐
                                       │Observability│
                                       │   SHAKTI    │
                                       └─────────────┘


              CAPABILITY ECOSYSTEM

              ┌──────────────────────┐
              │ Capability Registry  │
              │ Foundation           │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Canonical Capability │
              │ Convergence          │
              └──────────┬───────────┘
                         │
                         ▼
                 Runtime Integration


               KNOWLEDGE ECOSYSTEM

              ┌──────────────────────┐
              │ MASTERDB Ingestion   │
              │ Certification        │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Certified Knowledge  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ UniGuru              │
              │ Knowledge Retrieval  │
              └──────────┬───────────┘
                         │
                         ▼
                 Knowledge Contribution
```

---

# 17. Upstream / Downstream Relationships

## Constitutional Chain

```text
Sovereign Core
      ↓
RAJYA
      ↓
DGIC
      ↓
Runtime Reference Implementation
```

These are assignment-level constitutional dependencies.

---

## Runtime Chain

```text
Runtime Reference Implementation
      ↓
Execution Infrastructure
      ↓
SVACS Unified Core
      ↓
State / Replay / Evidence / Observability
```

---

## Evidence Chain

```text
Runtime Execution
      ↓
Runtime Evidence
      ↓
BHIV Bucket
      ↓
Persistent Artifact / Integrity
```

---

## Operational Visibility Chain

```text
Runtime Services
      ↓
Telemetry / Health
      ↓
SHAKTI
      ↓
Operator / Operational Visibility
```

---

## Capability Chain

```text
Capability Registry Foundation
      ↓
Canonical Capability Convergence
      ↓
Runtime Integration
```

---

## Knowledge Chain

```text
Data / Knowledge Package
      ↓
MASTERDB Certification
      ↓
Certified Knowledge
      ↓
UniGuru
      ↓
Knowledge Contribution
```

---

# 18. Adjacent Layer Summary

| Participant                      | Permanent Constitutional Home | Upstream            | Downstream                                | Adjacent Layers                 |
| -------------------------------- | ----------------------------- | ------------------- | ----------------------------------------- | ------------------------------- |
| Sovereign Core                   | Constitutional                | —                   | RAJYA                                     | Constitutional control          |
| RAJYA                            | Constitutional Integration    | Sovereign Core      | DGIC                                      | Sovereign / DGIC                |
| DGIC                             | Constitutional Integration    | RAJYA               | Runtime                                   | Runtime / control               |
| Runtime Reference Implementation | Runtime                       | DGIC                | Execution Infrastructure                  | Constitutional / execution      |
| SVACS Unified Core               | Execution Infrastructure      | Runtime             | State / Replay / Evidence / Observability | Runtime / execution             |
| Capability Registry Foundation   | Capability Registry           | Capability identity | Capability consumers                      | Capability composition          |
| Canonical Capability Convergence | Capability Composition        | Capability Registry | Runtime integration                       | Capability / runtime            |
| BHIV Bucket                      | Evidence Infrastructure       | Runtime / Replay    | Persistent evidence                       | Replay / integrity              |
| SHAKTI                           | Operational Observability     | Runtime services    | Operator                                  | Evidence / telemetry            |
| MASTERDB Certification           | Knowledge Certification       | Data packages       | Certified knowledge                       | MDU / knowledge                 |
| UniGuru                          | Knowledge                     | Certified knowledge | Knowledge consumers                       | Knowledge graph / documentation |

---

# 19. Constitutional Boundary Rules

## Rule 1 — Execution vs Registry

```text
Capability Registry
        ≠
Runtime Execution
```

The Capability Registry records capability identity and metadata.

Runtime execution remains within the runtime execution infrastructure.

---

## Rule 2 — Execution vs Dashboard

```text
Runtime
   ≠
SHAKTI
```

SHAKTI displays and aggregates runtime information.

It does not become the runtime execution authority.

---

## Rule 3 — Execution vs Evidence Storage

```text
Runtime
   ≠
BHIV Bucket
```

The runtime produces evidence.

Bucket persists and provides evidence/artifact storage and integrity mechanisms.

---

## Rule 4 — Execution vs Knowledge

```text
Runtime Execution
        ≠
Knowledge Retrieval
```

Runtime execution and knowledge retrieval remain separate constitutional responsibilities.

---

## Rule 5 — Certification vs Execution

```text
MASTERDB Certification
        ≠
Runtime Execution
```

Certification determines whether a package satisfies its certification boundary.

It does not execute the runtime.

---

## Rule 6 — Composition vs Execution

```text
Capability Composition
        ≠
Universal Runtime Execution
```

Capability composition and integration patterns do not transfer execution authority.

---

# 20. Plug-and-Play Constitutional Position

The Runtime Reference Implementation is considered constitutionally positioned for plug-and-play participation when:

1. Its constitutional identity is independently defined.
2. Its authority boundary is explicit.
3. Its upstream constitutional dependency is known.
4. Its downstream runtime infrastructure is known.
5. Runtime contracts are documented.
6. Registry participation is defined.
7. Replay participation is defined.
8. Evidence production is defined.
9. Observability participation is defined.
10. Knowledge contribution is defined where applicable.
11. No existing constitutional participant has its authority duplicated.

The DRF assignment establishes these positioning requirements without modifying the underlying runtime implementation.

---

# 21. Evidence Boundary

The assignment identifies the following as constitutional dependencies:

* Sovereign Core
* RAJYA
* DGIC
* TMS
* GC
* MDU

DRF does not invent implementation-level APIs, events, schemas, or authorities for these dependencies without direct repository evidence.

Similarly, repositories from the BHEX population that have not been sufficiently inspected remain candidates or unresolved participants rather than receiving invented constitutional identities.

---

# 22. BHEX Repository Boundary

The BHEX repository population is the discovery source for this assignment.

A repository's presence in BHEX does not automatically make it a runtime participant.

Only repositories with sufficient evidence of runtime, registry, capability, evidence, observability, certification, or knowledge responsibilities are given a constitutional position in this map.

The current high-confidence positioning includes:

* SHAKTI Runtime Integration and Operational Command Center
* Capability Registry Foundation
* Canonical Capability Convergence
* SVACS Unified Core
* MASTERDB Ingestion Certification Service
* UniGuru

Other repositories remain candidates or unresolved until sufficient evidence is available.

---

# 23. Phase Completion

**Assignment:** Distributed Relay Framework (DRF)

**Phase:** Runtime Ecosystem Positioning

**Artifact:** Runtime Participation Map

**Objective:** Permanently position the Runtime Reference Implementation and its confirmed adjacent participants within the TANTRA/BHIV Living Organism.

**Status:** Constitutional placement established using evidence-bounded positioning.

**Next Artifact:** Adjacent Layer Dependency Map.

```
```
