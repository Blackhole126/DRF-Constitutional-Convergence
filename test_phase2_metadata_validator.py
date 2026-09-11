import json
from pathlib import Path


def test_manifest_required_deliverables_are_present():
    root=Path(__file__).resolve().parents[1]
    manifest=json.loads((root/'drf_manifest.json').read_text())
    mapping={
      'Runtime Identity Cards':'docs/runtime-identity/RUNTIME_IDENTITY_CARDS.md',
      'Constitutional Authority Matrix':'docs/runtime-identity/CONSTITUTIONAL_AUTHORITY_MATRIX.md',
      'Runtime Participation Map':'docs/ecosystem-positioning/RUNTIME_PARTICIPATION_MAP.md',
      'Registry Participation Matrix':'docs/registry-participation/REGISTRY_PARTICIPATION_MATRIX.md',
      'Runtime Contract Documentation':'docs/runtime-contracts/RUNTIME_CONTRACTS.md',
      'Adjacent Layer Dependency Map':'docs/ecosystem-positioning/ADJACENT_LAYER_DEPENDENCY_MAP.md',
      'Replay & Evidence Model':'docs/evidence-replay/REPLAY_AND_EVIDENCE_MODEL.md',
      'Observability Model':'docs/observability/OBSERVABILITY_MODEL.md',
      'Knowledge Contribution Documentation':'docs/knowledge-contribution/KNOWLEDGE_CONTRIBUTION.md',
      'Runtime Convergence Report':'docs/RUNTIME_CONVERGENCE_REPORT.md',
      'REVIEW_PACKET.md':'REVIEW_PACKET.md',
    }
    assert all((root/mapping[x]).exists() for x in manifest['required_deliverables'])


def test_evidence_policy_forbids_invented_interfaces():
    root=Path(__file__).resolve().parents[1]
    manifest=json.loads((root/'drf_manifest.json').read_text())
    assert 'Do not invent undocumented interfaces' in manifest['evidence_policy']
