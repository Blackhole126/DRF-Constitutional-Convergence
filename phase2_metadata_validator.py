"""Deterministic Phase 2 metadata/contract evidence generator for the DRF convergence package."""
import hashlib, json, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'drf_manifest.json').read_text(encoding='utf-8'))
required=manifest.get('required_deliverables',[])
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and '.git' not in p.parts:
        files.append(p)
required_map={
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
checks={k:(ROOT/v).exists() for k,v in required_map.items()}
text='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in files if p.suffix in {'.md','.json'})
checks['evidence_policy_present']='evidence_policy' in manifest and 'Do not invent' in manifest['evidence_policy']
checks['tbd_policy_documented']='TBD' in text
checks['no_credentials_committed']=not any(re.search(r'(?i)(api[_-]?key|password|secret|bearer)\s*[:=]\s*["\']?[A-Za-z0-9_\-]{12,}', p.read_text(encoding='utf-8',errors='ignore')) for p in files if p.suffix in {'.md','.json','.py'})
metadata={'phase':'2','artifact':'DRF Constitutional Convergence','files_scanned':len(files),'required_deliverables':required,'checks':checks,'passed':all(checks.values()),'source_commit':None}
metadata['content_digest']=hashlib.sha256(json.dumps(metadata,sort_keys=True).encode()).hexdigest()
out=ROOT/'evidence/phase2/metadata_validation.json'; out.write_text(json.dumps(metadata,indent=2),encoding='utf-8'); print(json.dumps(metadata,indent=2))
