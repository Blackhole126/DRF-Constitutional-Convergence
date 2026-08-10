

# Runtime Contract Documentation

## 1. Purpose

This document defines the runtime interaction contracts required for the Distributed Relay Framework (DRF) Runtime Reference Implementation to participate as a reusable, plug-and-play participant within the TANTRA/BHIV ecosystem.

The assignment requires every runtime participant interaction to be documented.

This document therefore records:

- APIs
- Events consumed
- Events emitted
- SDK interfaces
- Attachment contracts
- Authentication
- Version compatibility
- Schema dependencies
- Contract ownership
- Contract evidence boundaries

Where the supplied repository evidence does not establish an implementation-level contract, the contract is explicitly marked as **Not Established** rather than invented.

---

# 2. Contract Principles

The DRF contract model follows these principles:

1. Every runtime interaction must have an identifiable interface.
2. Contract ownership must remain with the participant that owns the interface.
3. Consuming an API does not transfer authority.
4. Producing an event does not automatically make the producer the governance authority.
5. Authentication must be explicit.
6. Version compatibility must be explicit.
7. Schema dependencies must be documented.
8. Unsupported API paths must not be fabricated.
9. Placeholder or future interfaces must be clearly distinguished from implemented interfaces.
10. Contract gaps must remain visible until verified from authoritative repository evidence.

---

# 3. Contract Classification

Each contract is classified using the following statuses:

| Status | Meaning |
|---|---|
| Confirmed | Directly supported by supplied repository evidence |
| Documented | Described by repository documentation but implementation details require verification |
| Dependency | Required relationship established by the assignment |
| Not Established | Insufficient evidence to define the implementation contract |
| Future Verification | Contract requires direct inspection before production integration |

---

# 4. Runtime Reference Implementation Contract

## Constitutional Identity

**Runtime Reference Implementation**

## Contract Role

Primary reusable runtime participant.

## Upstream

```text
Sovereign Core
      ↓
RAJYA
      ↓
DGIC
      ↓
Runtime Reference Implementation
````

## Downstream

```text
Runtime Reference Implementation
      ↓
Execution Infrastructure
      ↓
Replay / Evidence / Observability
```

## API Contract

The assignment establishes that runtime contracts must be documented, but the supplied assignment material does not provide the authoritative API specification of the Runtime Reference Implementation.

Therefore:

**API:** Not Established from supplied evidence.

Implementation-specific endpoints must be extracted from the authoritative Runtime Reference Implementation repository before being declared as confirmed contracts.

## Events Consumed

**Not Established from supplied evidence.**

## Events Emitted

**Not Established from supplied evidence.**

## SDK Interface

**Not Established from supplied evidence.**

## Attachment Contract

The runtime must support attachment to the constitutional ecosystem through explicit contracts.

The exact attachment mechanism is:

**Not Established from supplied evidence.**

## Authentication

**Not Established from supplied evidence.**

No authentication mechanism should be invented.

## Version Compatibility

**Not Established from supplied evidence.**

The runtime integration must define a compatible contract version before production attachment.

## Schema Dependencies

Expected contract categories include:

* Runtime identity
* Runtime state
* Execution information
* Replay information
* Evidence/provenance
* Observability information

Exact schema names and versions require authoritative repository evidence.

---

# 5. SVACS Unified Core Contract

## Constitutional Identity

**SVACS Unified Core — Runtime Execution Infrastructure**

## Contract Role

Runtime execution infrastructure supporting execution, state, orchestration, replay, provenance, telemetry, validation, and runtime proof surfaces evidenced by the repository.

## Upstream Dependency

```text
Runtime Reference Implementation
        ↓
SVACS Unified Core
```

## Downstream Dependencies

```text
SVACS Unified Core
        ├── Runtime State
        ├── Replay
        ├── Evidence
        └── Observability
```

## API Contract

The supplied repository evidence establishes the presence of runtime contract and API-oriented components, but this assignment document does not provide a complete endpoint inventory.

Therefore:

**API:** Documented at repository level; exact production endpoint inventory requires direct implementation verification.

## Events Consumed

Runtime execution events required by the implementation.

**Exact event names:** Not Established from supplied evidence.

## Events Emitted

The implementation is described as producing runtime/proof/telemetry/provenance information.

**Exact event names and schemas:** Not Established from supplied evidence.

## SDK Interface

**Not Established from supplied evidence.**

## Attachment Contract

The runtime must attach through the documented execution/runtime contracts of SVACS Unified Core.

Exact attachment interface requires authoritative implementation inspection.

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

**Not Established from supplied evidence.**

## Schema Dependencies

Repository evidence indicates dependencies around:

* Runtime execution
* State
* Replay
* Provenance
* Telemetry
* Runtime proof
* Validation

Exact schema identifiers require direct repository verification.

---

# 6. Runtime State Contract

## Contract Owner

**SVACS Unified Core**

## Contract Purpose

Represent and maintain state required by the runtime execution chain.

## API

**Not Established from supplied evidence.**

## Events Consumed

**Not Established from supplied evidence.**

## Events Emitted

**Not Established from supplied evidence.**

## SDK

**Not Established from supplied evidence.**

## Authentication

Inherited from the runtime infrastructure contract where applicable.

Exact mechanism is not established.

## Version Compatibility

State schema version must remain compatible with the runtime execution contract.

Exact version is not established.

## Schema Dependencies

The state contract must define, at minimum:

* Runtime identifier
* Execution/session identifier
* State identifier
* State status
* Timestamp
* Version
* Provenance/reference information where applicable

These are contract requirements, not claims that these exact fields currently exist.

---

# 7. Replay Contract

## Contract Owner

**SVACS Unified Core**

## Supporting Participant

**BHIV Bucket**

## Contract Purpose

Support replay and reconstruction of runtime activity.

## API

**Not Established from supplied evidence.**

## Events Consumed

Runtime execution/state events required to reconstruct the relevant runtime sequence.

Exact event names are not established.

## Events Emitted

Replay result/state information where implemented.

Exact event names are not established.

## SDK Interface

**Not Established from supplied evidence.**

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

Replay schema must remain compatible with the execution and state schema versions.

## Schema Dependencies

Replay depends on:

* Runtime identity
* Execution identity
* Event identity
* Event ordering
* Timestamp information
* State information
* Provenance references
* Evidence references

Exact schema implementation requires verification.

---

# 8. Evidence Contract

## Primary Contract Owner

**BHIV Bucket**

## Evidence Producer

**SVACS Unified Core / Runtime**

## Contract Purpose

Persist and retrieve runtime artifacts and evidence.

## API

The supplied evidence establishes Bucket as an artifact/evidence service.

**Exact endpoint inventory:** Not Established from supplied evidence in this assignment.

## Events Consumed

Evidence/artifact persistence requests or runtime evidence events.

Exact event names are not established.

## Events Emitted

Artifact persistence/verification results where implemented.

Exact event names are not established.

## SDK Interface

**Not Established from supplied evidence.**

## Attachment Contract

Runtime evidence must be attachable to:

* Runtime identity
* Execution identity
* Replay identity
* Provenance information

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

Evidence schema must remain compatible with the producing runtime and replay schemas.

## Schema Dependencies

Minimum conceptual evidence relationships:

```text
Runtime Identity
      ↓
Execution Identity
      ↓
Evidence Artifact
      ↓
Provenance
      ↓
Storage / Integrity
```

Exact field names require implementation verification.

---

# 9. SHAKTI Observability Contract

## Contract Owner

**SHAKTI**

## Contract Role

Passive operational visibility consumer.

## Architecture Evidence

The supplied SHAKTI documentation explicitly describes the dashboard as a standalone frontend SPA that consumes multiple external microservices.

The documentation identifies dedicated clients for services including:

* Control Plane
* Karma
* Setu
* Niyantran
* Prana
* Bucket
* InsightFlow
* Rajya
* Tantra
* Sanskar
* Keshav

## Confirmed API Pattern

SHAKTI uses dedicated Axios clients and React Query hooks.

The supplied documentation identifies examples including:

```text
GET /health
GET /system/status
GET /metrics
GET /dashboard/executive
GET /dashboard/operations
GET /dashboard/alerts
GET /dashboard/runtime
GET /dashboard/telemetry
GET /intelligence/lineage
GET /projects
GET /prana/propagation-log
GET /bucket/artifacts
GET /bucket/storage-stats
GET /health
GET /ranking
```

These endpoints belong to the respective backend services consumed by SHAKTI.

SHAKTI is not the authority for those backend services.

## Events Consumed

SHAKTI primarily consumes API responses and query data.

Exact event-stream contracts are:

**Not Established from supplied evidence.**

## Events Emitted

SHAKTI does not establish runtime execution events in the supplied architecture.

Operational UI actions/events may exist, but exact contracts are:

**Not Established.**

## SDK Interface

React Query and Axios are the documented client integration mechanisms.

## Authentication

The supplied SHAKTI documentation states:

> Currently, auth is mocked on the frontend for development speed.

The documented integration points are:

```text
src/hooks/useAuth.ts
src/hooks/useAuthorization.ts
```

Real JWT/OAuth integration is described as a future replacement point.

## Version Compatibility

The supplied SHAKTI stack specifies:

* React 19
* TypeScript 6
* Vite 8
* TanStack Query 5
* Tailwind CSS 4

Backend API version compatibility is not fully established by the supplied documentation.

## Schema Dependencies

The documentation identifies:

```text
src/types/api.ts
src/types/runtime.ts
src/types/setu.ts
```

as TypeScript schema/interface locations.

---

# 10. Capability Registry Contract

## Contract Owner

**Capability Registry Foundation**

## Contract Role

Capability registration and metadata authority.

## API

The repository evidence establishes a registry service and API-oriented capability management.

Exact production endpoints are:

**Not Established from supplied evidence.**

## Events Consumed

Capability registration/update requests where implemented.

Exact event names are not established.

## Events Emitted

Capability registration/status changes where implemented.

Exact event names are not established.

## SDK Interface

**Not Established from supplied evidence.**

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

Capability metadata must support version identification.

Exact compatibility rules require repository verification.

## Schema Dependencies

The capability registry requires metadata categories such as:

* Capability identifier
* Name
* Description
* Version
* Category
* Status
* Dependencies

Exact schema fields require direct repository verification.

---

# 11. Canonical Capability Convergence Contract

## Contract Owner

**Canonical Capability Convergence**

## Contract Role

Reusable capability composition and integration.

## API

The repository documentation establishes standardized API/interface patterns.

Exact endpoint inventory:

**Not Established from supplied evidence.**

## Events Consumed

Capability lifecycle/dependency information where implemented.

Exact events are not established.

## Events Emitted

Capability lifecycle/integration information where implemented.

Exact events are not established.

## SDK Interface

Standardized capability contracts are documented conceptually.

Exact SDK package/interface names require repository verification.

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

Capability versions must remain compatible with their declared contracts and dependencies.

Exact versioning mechanism requires verification.

## Schema Dependencies

* Capability identity
* Capability version
* Capability lifecycle
* Dependency metadata
* Integration contract

---

# 12. MASTERDB Certification Contract

## Contract Owner

**MASTERDB Ingestion Certification Service**

## Contract Role

Validation, certification and lifecycle management of knowledge/data packages.

## API

Repository documentation establishes endpoint categories for:

* Validation
* Certification
* Registry
* Knowledge objects
* Retrieval
* Replay/audit
* MDU compatibility
* TANTRA dataset registration

Exact production endpoint paths and methods must be verified against the repository implementation.

## Events Consumed

Package submission and validation-related information.

Exact event names are not established.

## Events Emitted

Certification state/lifecycle changes where implemented.

Exact event names are not established.

## SDK Interface

**Not Established from supplied evidence.**

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

Certification and knowledge schemas must remain compatible with the relevant MDU/TANTRA contracts.

Exact versions require verification.

## Schema Dependencies

Conceptual dependencies include:

* Package identity
* Package version
* Validation state
* Certification state
* Provenance
* Knowledge object
* Audit/replay information
* MDU compatibility

---

# 13. UniGuru Contract

## Contract Owner

**UniGuru**

## Contract Role

Deterministic knowledge retrieval.

## API

The supplied repository evidence identifies a deterministic retrieval service and `/new_rag` surface.

Exact endpoint inventory requires repository verification.

## Events Consumed

Knowledge retrieval requests and associated knowledge identifiers.

Exact event names are not established.

## Events Emitted

Knowledge retrieval results.

Exact event names are not established.

## SDK Interface

**Not Established from supplied evidence.**

## Authentication

**Not Established from supplied evidence.**

## Version Compatibility

Knowledge schema and retrieval interface must remain compatible with the certified knowledge source.

## Schema Dependencies

The supplied evidence identifies:

* Kosha schema
* Knowledge IDs
* Knowledge-graph artifacts
* Knowledge retrieval structures

Exact schema versions require verification.

---

# 14. TMS Contract

## Assignment Role

Constitutional dependency.

## API

Not established.

## Events

Not established.

## Authentication

Not established.

## Version Compatibility

Not established.

## Schema Dependencies

Not established.

## DRF Boundary

DRF must integrate with the authoritative TMS contract when provided.

No TMS implementation is invented in this assignment.

---

# 15. GC Contract

## Assignment Role

Constitutional dependency.

## API

Not established.

## Events

Not established.

## Authentication

Not established.

## Version Compatibility

Not established.

## Schema Dependencies

Not established.

## DRF Boundary

DRF must integrate with the authoritative GC contract when provided.

No GC implementation is invented in this assignment.

---

# 16. MDU Contract

## Assignment Role

Constitutional dependency.

## API

Not established by the supplied assignment.

## Events

Not established.

## Authentication

Not established.

## Version Compatibility

Not established.

## Schema Dependencies

The MASTERDB certification service documentation indicates MDU compatibility as an integration concern.

Exact MDU schema/version remains to be verified from authoritative implementation evidence.

---

# 17. Authentication Contract Matrix

| Participant                      | Authentication Status             | Evidence                                |
| -------------------------------- | --------------------------------- | --------------------------------------- |
| Runtime Reference Implementation | Not Established                   | Authoritative runtime contract required |
| SVACS Unified Core               | Not Established                   | Implementation verification required    |
| Replay                           | Not Established                   | Implementation verification required    |
| BHIV Bucket                      | Not Established                   | Implementation verification required    |
| SHAKTI                           | Development authentication mocked | Supplied SHAKTI documentation           |
| Capability Registry Foundation   | Not Established                   | Implementation verification required    |
| Canonical Capability Convergence | Not Established                   | Implementation verification required    |
| MASTERDB Certification           | Not Established                   | Implementation verification required    |
| UniGuru                          | Not Established                   | Implementation verification required    |
| TMS                              | Not Established                   | Constitutional dependency               |
| GC                               | Not Established                   | Constitutional dependency               |
| MDU                              | Not Established                   | Constitutional dependency               |

---

# 18. Version Compatibility Matrix

| Contract                           | Required Compatibility                    | Current Evidence                                              |
| ---------------------------------- | ----------------------------------------- | ------------------------------------------------------------- |
| Runtime ↔ Execution Infrastructure | Runtime contract compatibility            | Requires verification                                         |
| Execution ↔ State                  | State schema compatibility                | Requires verification                                         |
| Execution ↔ Replay                 | Event/schema compatibility                | Requires verification                                         |
| Replay ↔ Evidence                  | Evidence/provenance compatibility         | Requires verification                                         |
| Runtime ↔ Observability            | Telemetry/API compatibility               | SHAKTI service clients documented                             |
| Capability ↔ Registry              | Capability metadata/version compatibility | Registry purpose documented                                   |
| Capability ↔ Composition           | Capability contract compatibility         | Composition contract documented conceptually                  |
| Certification ↔ MDU                | MDU schema compatibility                  | Compatibility identified; exact version requires verification |
| Certification ↔ TANTRA             | Dataset/contract compatibility            | Integration identified; exact version requires verification   |
| MASTERDB ↔ UniGuru                 | Knowledge schema compatibility            | Requires verification                                         |

---

# 19. Schema Dependency Matrix

| Participant                      | Primary Schema Dependencies                                      |
| -------------------------------- | ---------------------------------------------------------------- |
| Runtime Reference Implementation | Runtime identity, execution, state, replay, evidence             |
| SVACS Unified Core               | Execution, state, replay, provenance, telemetry, proof           |
| Replay                           | Execution events, state, timestamps, provenance                  |
| BHIV Bucket                      | Artifact metadata, evidence, provenance, integrity               |
| SHAKTI                           | API response types, runtime types, service-specific schemas      |
| Capability Registry              | Capability identity, metadata, category, version                 |
| Canonical Capability Convergence | Capability contract, lifecycle, dependency metadata              |
| MASTERDB Certification           | Package, certification, provenance, knowledge-object, MDU/TANTRA |
| UniGuru                          | Kosha, knowledge IDs, retrieval and graph structures             |
| TMS                              | Not established                                                  |
| GC                               | Not established                                                  |
| MDU                              | Not established                                                  |

---

# 20. Attachment Contract

A runtime participant must be attachable to the constitutional ecosystem without requiring a redesign of the existing runtime.

The conceptual attachment model is:

```text
Runtime Identity
      ↓
Capability / Contract Identity
      ↓
Runtime Interface
      ↓
Execution Participation
      ↓
Replay Participation
      ↓
Evidence Production
      ↓
Observability
      ↓
Registry / Knowledge Contribution
```

An attachment must preserve:

* Identity
* Contract version
* Authority boundary
* Dependency declaration
* Authentication requirements
* Schema compatibility
* Provenance
* Health status

---

# 21. Contract Ownership Rules

## Runtime

Owns its runtime-specific contracts.

## Execution Infrastructure

Owns execution infrastructure contracts.

## Registry

Owns registry contracts.

## Evidence Storage

Owns artifact persistence contracts.

## Observability

Owns dashboard/observability consumption contracts.

## Certification

Owns certification contracts.

## Knowledge

Owns knowledge retrieval contracts.

A consumer must not redefine a provider's contract.

---

# 22. Failure and Compatibility Boundary

When a dependency is unavailable:

1. The consumer must not silently claim the dependency succeeded.
2. The failure must remain observable.
3. Cached or previous data may be retained only where explicitly supported.
4. Evidence must preserve the failure state where evidence is part of the contract.
5. Replay must distinguish successful execution from failed execution.
6. Authentication failures must remain distinguishable from transport failures.
7. Schema incompatibility must not be silently converted into a successful response.

The exact implementation behavior must be taken from each authoritative participant.

---

# 23. Contract Gap Register

The following items require direct repository verification before being treated as production-confirmed:

| Gap                                            | Required Evidence                   |
| ---------------------------------------------- | ----------------------------------- |
| Runtime Reference Implementation API inventory | Runtime repository                  |
| Runtime event catalogue                        | Runtime repository                  |
| Runtime SDK interface                          | Runtime repository                  |
| Runtime authentication                         | Runtime repository/configuration    |
| Runtime schema versions                        | Runtime repository                  |
| SVACS exact endpoints                          | SVACS implementation                |
| SVACS exact event schemas                      | SVACS implementation                |
| Replay endpoint/event catalogue                | Replay implementation               |
| Bucket endpoint catalogue                      | Bucket implementation               |
| Bucket authentication                          | Bucket implementation               |
| Capability Registry endpoint catalogue         | Registry implementation             |
| Capability Registry authentication             | Registry implementation             |
| Canonical Capability SDK                       | Canonical capability implementation |
| MASTERDB exact endpoint catalogue              | Certification implementation        |
| MASTERDB authentication                        | Certification implementation        |
| MDU contract version                           | Authoritative MDU source            |
| TMS contract                                   | Authoritative TMS source            |
| GC contract                                    | Authoritative GC source             |
| Sovereign Core contract                        | Authoritative Sovereign Core source |
| RAJYA contract                                 | Authoritative RAJYA source          |
| DGIC contract                                  | Authoritative DGIC source           |

---

# 24. No Undocumented Interaction Rule

Before production integration, every runtime interaction should be represented by:

```text
Provider
   ↓
Contract
   ↓
Consumer
   ↓
Authentication
   ↓
Schema
   ↓
Version
   ↓
Failure Behaviour
   ↓
Evidence / Observability
```

If any required field is unknown, the integration should be marked as requiring verification rather than documented as confirmed.

---

# 25. Plug-and-Play Contract Requirement

The Runtime Reference Implementation is contractually plug-and-play when:

* Its identity is known.
* Its provider/consumer relationships are known.
* Its APIs are documented.
* Its events are documented.
* Its SDK interface is documented where applicable.
* Its attachment mechanism is documented.
* Authentication is documented.
* Version compatibility is documented.
* Schema dependencies are documented.
* Evidence/provenance relationships are documented.
* Observability relationships are documented.
* Registry participation is documented.

The current DRF documentation establishes the contract framework and identifies remaining evidence gaps.

---

# 26. Acceptance Check

| Acceptance Requirement                                  | Status |
| ------------------------------------------------------- | ------ |
| APIs identified or explicitly marked unknown            | PASS   |
| Events consumed identified or explicitly marked unknown | PASS   |
| Events emitted identified or explicitly marked unknown  | PASS   |
| SDK interfaces identified or explicitly marked unknown  | PASS   |
| Attachment contracts identified                         | PASS   |
| Authentication documented or marked unknown             | PASS   |
| Version compatibility documented                        | PASS   |
| Schema dependencies documented                          | PASS   |
| Contract ownership defined                              | PASS   |
| Contract gaps explicitly recorded                       | PASS   |
| No unsupported API invented                             | PASS   |
| No undocumented interaction treated as confirmed        | PASS   |

---

# 27. Status

**Assignment:** Distributed Relay Framework (DRF)

**Artifact:** Runtime Contract Documentation

**Status:** Contract framework established with unsupported implementation details explicitly marked for verification.

**Next Artifact:** Registry Participation Matrix.

```
```
