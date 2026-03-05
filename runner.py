import json, time
from pathlib import Path

def run_profile(iterations: int = 5, base_start_ms: int = 2800, jitter_ms: int = 600):
    samples = []
    for i in range(iterations):
        # deterministic-ish synthetic timing model for MVP
        t = base_start_ms + ((i * 137) % jitter_ms)
        reload_t = int(t * 0.42)
        samples.append({"run": i + 1, "startup_ms": t, "reload_ms": reload_t})
    return samples

def save_session(path: Path, samples, label: str):
    payload = {"label": label, "samples": samples}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding='utf-8')
