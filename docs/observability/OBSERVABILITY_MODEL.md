
# Observability Model

## 1. Purpose

This document defines the observability position of the Distributed Relay Framework (DRF) within the TANTRA/BHIV Living Organism.

The objective is to make runtime health, execution status, telemetry, logs, evidence, replay state, dependency health, and production indicators observable without creating a second runtime or observability authority.

DRF does not redesign the existing observability infrastructure.

It documents how existing runtime participants contribute to and consume observability information.

---

# 2. Observability Principles

1. Runtime execution remains owned by the runtime authority.
2. Observability is a visibility and diagnostic capability.
3. Observability must not become an alternate execution path.
4. Every important runtime participant should expose an identifiable health/telemetry surface where applicable.
5. Runtime evidence and observability should remain traceable to runtime identity.
6. Failures must remain distinguishable from healthy states.
7. Observability consumers must not modify authoritative runtime state unless explicitly authorized.
8. Dashboard visibility does not imply operational execution authority.
9. Metrics, logs and telemetry must retain sufficient provenance.
10. Unsupported implementation details are marked for verification rather than invented.

---

# 3. Constitutional Position

The observability position is:

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
Telemetry / Logs / Health
      ↓
SHAKTI
      ↓
Operational Visibility
````

SHAKTI is positioned downstream of runtime services as an operational visibility surface.

---

# 4. Observability Layers

The DRF observability model consists of:

1. Runtime Health
2. Execution Metrics
3. Runtime Metrics
4. Logs
5. Telemetry
6. Replay Visibility
7. Evidence Visibility
8. Dependency Health
9. Dashboard Visibility
10. Production Health Indicators

---

# 5. Runtime Health Model

Every runtime participant should have a recognizable health state.

Conceptually:

```text
UNKNOWN
   ↓
STARTING
   ↓
HEALTHY
   ↓
DEGRADED
   ↓
UNAVAILABLE
```

Recovery:

```text
UNAVAILABLE
   ↓
RECOVERING
   ↓
HEALTHY
```

These are conceptual health states.

Exact implementation status names must be verified against the authoritative runtime implementation.

---

# 6. Runtime Health Information

A runtime health record should conceptually identify:

```text
Runtime ID
Runtime Version
Health Status
Timestamp
Dependency Status
Execution Status
Replay Status
Evidence Status
Telemetry Status
```

The exact production schema is implementation-specific.

---

# 7. Execution Observability

Runtime execution should be observable through:

* execution status
* execution duration
* execution outcome
* execution identity
* runtime identity
* dependency state
* relevant errors
* evidence references
* replay references

Conceptual flow:

```text
Runtime Execution
      ↓
Execution State
      ↓
Execution Metrics
      ↓
Telemetry
      ↓
Operational Visibility
```

---

# 8. Runtime Metrics

Recommended conceptual runtime metrics include:

| Metric                    | Purpose                                          |
| ------------------------- | ------------------------------------------------ |
| Execution count           | Measure runtime activity                         |
| Successful executions     | Measure successful operation                     |
| Failed executions         | Detect runtime failures                          |
| Execution latency         | Measure execution performance                    |
| Active executions         | Measure current runtime load                     |
| Replay count              | Measure replay activity                          |
| Replay failures           | Detect replay problems                           |
| Evidence generation count | Measure proof production                         |
| Evidence failures         | Detect evidence problems                         |
| Dependency failures       | Detect downstream/upstream availability problems |
| Health state              | Measure runtime availability                     |

These are observability requirements.

Exact metric names and instrumentation mechanisms must be verified from implementation.

---

# 9. Performance Indicators

Runtime performance should be observable through appropriate indicators such as:

```text
Latency
Throughput
Error Rate
Availability
Resource Utilization
Queue/Workload State
Dependency Latency
Replay Duration
Evidence Persistence Duration
```

No new runtime functionality is required solely to document these indicators.

---

# 10. Logs

Logs provide detailed diagnostic context.

Conceptually:

```text
Timestamp
Runtime ID
Execution ID
Severity
Component
Event / Message
Correlation ID
Error Information
Provenance Reference
```

Logs should allow an operator or reviewer to associate an observed problem with the corresponding runtime execution.

Exact log schema is implementation-specific.

---

# 11. Log Severity

A conventional conceptual severity model is:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

The actual runtime logging framework and severity vocabulary must remain authoritative.

---

# 12. Correlation and Traceability

Observability records should be traceable through common runtime identifiers where supported.

Conceptual relationship:

```text
Runtime ID
    │
    ├── Execution ID
    │
    ├── Event ID
    │
    ├── Replay ID
    │
    ├── Evidence ID
    │
    └── Artifact ID
```

This creates an observable lineage from runtime activity to evidence.

---

# 13. Telemetry Model

Telemetry provides machine-readable operational information.

Conceptually:

```text
Runtime
  ↓
Telemetry
  ├── Metrics
  ├── Logs
  ├── Traces
  └── Health
```

Telemetry must preserve enough identity information to associate the observation with the correct runtime participant.

---

# 14. Trace Model

Where distributed tracing is supported, the conceptual model is:

```text
Request / Execution
       ↓
Trace
       ↓
Span
       ↓
Runtime Component
       ↓
Dependency
```

The exact tracing technology and span schema are not established by the supplied assignment material.

---

# 15. Dependency Observability

A runtime participant should expose the health of important dependencies where supported.

Conceptually:

```text
Runtime
  │
  ├── State
  ├── Replay
  ├── Evidence
  ├── Registry
  └── External Service
```

Each dependency may have:

```text
AVAILABLE
DEGRADED
UNAVAILABLE
UNKNOWN
```

The runtime must not claim healthy operation when a critical dependency failure prevents the relevant capability from functioning.

---

# 16. Replay Observability

Replay activity should be observable through:

* replay status
* replay identifier
* associated execution
* replay duration
* replay result
* replay failure
* verification state

Conceptual flow:

```text
Execution
   ↓
Replay
   ↓
Replay Status
   ↓
Telemetry
   ↓
SHAKTI
```

Replay observability does not transfer execution authority to the dashboard.

---

# 17. Evidence Observability

Evidence production should be observable through:

* evidence generated
* evidence persisted
* evidence verification
* persistence failures
* provenance availability
* artifact references

Conceptual flow:

```text
Runtime
   ↓
Evidence
   ↓
Persistence
   ↓
Verification
   ↓
Telemetry
```

---

# 18. SHAKTI Observability Role

## Participant

**SHAKTI Executive Dashboard Capability**

## Constitutional Layer

Operational / Observability Surface

## Primary Role

Provide operational visibility over runtime and ecosystem services.

The supplied SHAKTI architecture explicitly describes it as a standalone frontend SPA and passive consumer of external microservices.

Therefore:

```text
SHAKTI = Observability Consumer
```

not:

```text
SHAKTI = Runtime Execution Authority
```

---

# 19. SHAKTI Service Visibility

The supplied SHAKTI documentation identifies dedicated clients for:

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

These service relationships form the dashboard's operational visibility surface.

---

# 20. SHAKTI Health Surfaces

The supplied documentation identifies service-facing health/status examples including:

```text
GET /health
GET /system/status
GET /metrics
GET /dashboard/runtime
GET /dashboard/telemetry
```

Additional service-specific health endpoints are documented in the SHAKTI integration material.

These endpoints belong to their respective services.

SHAKTI consumes their responses.

---

# 21. SHAKTI Runtime Dashboard

The supplied architecture identifies a dedicated:

**Runtime Health**

layout.

The dashboard also identifies:

**Simulation Replay**

and:

**Evidence**

as dedicated operational surfaces.

This establishes a visibility path for runtime health, replay and evidence information.

---

# 22. SHAKTI Resilience Model

The supplied SHAKTI documentation identifies:

* Error Boundaries
* React Query
* `keepPreviousData`
* retries
* exponential backoff
* request timeouts
* offline indicators
* stale data warnings

The architecture states that a backend failure should not cause the entire dashboard to crash.

Conceptually:

```text
Backend Failure
      ↓
Query Error
      ↓
Cached Data Retained
      ↓
Offline / Stale Indicator
      ↓
Other Dashboard Zones Continue
```

This is a dashboard resilience mechanism.

It does not alter backend runtime authority.

---

# 23. Graceful Degradation

The supplied SHAKTI documentation states that dashboard queries use:

```text
placeholderData: keepPreviousData
```

where applicable.

This allows previously available data to remain visible while a background request fails.

The UI can indicate:

* stale data
* offline status
* failed service
* degraded state

---

# 24. Error Isolation

The SHAKTI architecture states that every layout is protected by a discrete error boundary.

Conceptual model:

```text
Dashboard
 ├── Zone A → Error Boundary
 ├── Zone B → Error Boundary
 ├── Zone C → Error Boundary
 └── Zone D → Error Boundary
```

A failure in one zone should not necessarily crash the entire dashboard.

This supports operational resilience.

---

# 25. Authentication Observability

The supplied SHAKTI documentation states that frontend authentication is currently mocked for development.

Documented integration points include:

```text
src/hooks/useAuth.ts
src/hooks/useAuthorization.ts
```

The documentation describes replacement with standard JWT decoding or an OAuth provider for real backend integration.

Therefore:

**Current authentication status: Development/mock.**

Authentication productionization is outside this constitutional convergence assignment unless separately assigned.

---

# 26. Production Health Indicators

The production observability model should expose indicators covering:

### Availability

```text
Runtime availability
Dependency availability
Service availability
```

### Reliability

```text
Error rate
Failed executions
Failed replay operations
Failed evidence persistence
```

### Performance

```text
Execution latency
Dependency latency
Replay duration
Evidence persistence duration
```

### Integrity

```text
Evidence verification
Provenance completeness
Replay verification
Schema compatibility
```

### Operational State

```text
Healthy
Degraded
Unavailable
Recovering
```

---

# 27. Observability Authority Matrix

| Responsibility                  | Primary Participant             | Not Owned      |
| ------------------------------- | ------------------------------- | -------------- |
| Runtime execution               | Runtime infrastructure          | SHAKTI         |
| Runtime state                   | Runtime infrastructure          | SHAKTI         |
| Runtime telemetry production    | Runtime infrastructure          | Dashboard      |
| Evidence production             | Runtime/evidence infrastructure | Dashboard      |
| Evidence persistence            | Bucket                          | Dashboard      |
| Replay execution/reconstruction | Replay infrastructure           | Dashboard      |
| Operational presentation        | SHAKTI                          | Runtime engine |
| Review decision                 | Review process                  | SHAKTI         |
| Knowledge certification         | MASTERDB Certification          | SHAKTI         |

---

# 28. Observability Dependency Map

```text
                   Runtime
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        State       Replay      Evidence
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Telemetry
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        Metrics      Logs       Traces
          │           │           │
          └───────────┼───────────┘
                      ▼
                    SHAKTI
                      │
                      ▼
                   Operator
```

---

# 29. Runtime → Observability Contract

Conceptual contract:

```text
Runtime ID
Execution ID
Health State
Execution State
Telemetry
Metrics
Logs
Trace References
Evidence References
Replay References
Timestamp
```

The exact contract is implementation-specific and must be verified against the authoritative runtime source.

---

# 30. Observability Failure Model

Observability failure should not automatically imply runtime failure.

For example:

```text
Runtime = HEALTHY
Observability = DEGRADED
```

may be valid when runtime execution continues but telemetry/dashboard access is unavailable.

Similarly:

```text
Runtime = DEGRADED
Observability = HEALTHY
```

may indicate that the monitoring system is correctly reporting a runtime problem.

The two states must remain logically separate.

---

# 31. Critical Dependency Failure

Where a dependency is required for runtime correctness:

```text
Critical Dependency Failure
        ↓
Runtime State Change
        ↓
Health / Error Evidence
        ↓
Telemetry
        ↓
Operational Visibility
```

The runtime should not report successful operation solely because the dashboard remains available.

---

# 32. Observability and Evidence Relationship

Observability and evidence are related but distinct.

### Evidence

Answers:

> What happened?

### Observability

Answers:

> What is happening and how is the system behaving?

Relationship:

```text
Execution
   ├── Evidence → Historical proof
   │
   └── Telemetry → Operational visibility
```

Neither replaces the other.

---

# 33. Observability and Replay Relationship

Replay and observability are also distinct.

### Replay

Reconstructs or inspects historical execution.

### Observability

Monitors current and historical operational state.

```text
Historical Execution
      ├── Replay
      └── Evidence

Current / Operational State
      └── Observability
```

---

# 34. Metrics Ownership

Metrics should remain owned by the participant that produces the underlying measurement.

For example:

```text
Runtime execution metric
        ↓
Runtime infrastructure

Storage metric
        ↓
Storage service

Dashboard rendering metric
        ↓
SHAKTI
```

A dashboard may aggregate metrics without becoming their owner.

---

# 35. Log Ownership

Logs should remain attributable to their source component.

Conceptually:

```text
Runtime Log
      ↓
Runtime

Storage Log
      ↓
Bucket

Dashboard Log
      ↓
SHAKTI
```

Cross-service aggregation must preserve source identity.

---

# 36. Telemetry Provenance

Telemetry should preserve:

* source runtime
* component
* timestamp
* execution/correlation reference where applicable
* metric/log/trace type

This enables the operator to distinguish observations from different participants.

---

# 37. Observability and Registry Relationship

Registry metadata should make runtime identity discoverable.

Conceptually:

```text
Runtime Registry
      ↓
Runtime Identity
      ↓
Observability
      ↓
Health / Metrics / Logs
```

The registry identifies the participant.

Observability reports its operational state.

---

# 38. Observability and Review Relationship

Observability data can provide supporting evidence for review.

```text
Runtime
   ↓
Telemetry
   ↓
Operational Evidence
   ↓
Review Packet
```

Observability information does not automatically equal certification.

---

# 39. Observability and Knowledge Relationship

Selected validated operational evidence may contribute to reusable knowledge.

```text
Operational Evidence
      ↓
Validation / Certification
      ↓
Knowledge
```

Raw telemetry must not automatically be treated as trusted knowledge.

---

# 40. Production Readiness Indicators

A runtime participant should be considered operationally observable when:

* Runtime identity is known.
* Health state is available or explicitly documented as unavailable.
* Execution status is traceable.
* Important failures are visible.
* Metrics are attributable.
* Logs are attributable.
* Replay state is visible where replay exists.
* Evidence state is visible where evidence exists.
* Dependencies are observable where applicable.
* Dashboard/operational visibility is available where applicable.

---

# 41. Observability Gap Register

The following implementation details require authoritative verification:

| Gap                                       | Required Evidence                |
| ----------------------------------------- | -------------------------------- |
| Runtime health endpoint                   | Runtime implementation           |
| Runtime metric names                      | Runtime implementation           |
| Runtime log schema                        | Runtime implementation           |
| Runtime trace schema                      | Runtime implementation           |
| Replay telemetry                          | Replay implementation            |
| Evidence telemetry                        | Evidence implementation          |
| Bucket health/metrics                     | Bucket implementation            |
| Registry health                           | Registry implementation          |
| Exact SHAKTI production backend contracts | Backend implementations          |
| Production authentication                 | Deployment/backend configuration |
| Production alert thresholds               | Operational policy               |

---

# 42. No Duplicate Observability Authority

DRF must not introduce:

```text
Second Dashboard
Second Telemetry System
Second Logging Authority
Second Monitoring Authority
Second Runtime Health Authority
```

The assignment is constitutional convergence.

Existing observability participants remain authoritative.

---

# 43. Plug-and-Play Observability Requirement

The runtime is observability-ready when:

```text
Runtime Identity
      +
Health
      +
Execution Status
      +
Metrics
      +
Logs
      +
Telemetry
      +
Replay Visibility
      +
Evidence Visibility
      +
Dependency Visibility
      =
Operationally Observable Runtime
```

---

# 44. Acceptance Check

| Requirement                                     | Status |
| ----------------------------------------------- | ------ |
| Runtime health model defined                    | PASS   |
| Metrics model defined                           | PASS   |
| Logs model defined                              | PASS   |
| Telemetry model defined                         | PASS   |
| Replay observability defined                    | PASS   |
| Evidence observability defined                  | PASS   |
| Dependency health defined                       | PASS   |
| SHAKTI role defined                             | PASS   |
| Production indicators defined                   | PASS   |
| Observability authority boundaries defined      | PASS   |
| Evidence/observability distinction defined      | PASS   |
| Replay/observability distinction defined        | PASS   |
| Failure model defined                           | PASS   |
| No duplicate observability authority introduced | PASS   |
| Evidence gaps explicitly identified             | PASS   |

---

# 45. Status

**Assignment:** Distributed Relay Framework (DRF)

**Artifact:** Observability Model

**Status:** Runtime health, metrics, logs, telemetry, replay visibility, evidence visibility and operational dashboard positioning documented.

**Next Artifact:** Knowledge Contribution Documentation.

```
```
