def summarize(samples):
    if not samples:
        return {"avg_startup_ms": 0, "avg_reload_ms": 0, "peak_startup_ms": 0}
    avg_startup = sum(s['startup_ms'] for s in samples) / len(samples)
    avg_reload = sum(s['reload_ms'] for s in samples) / len(samples)
    peak_startup = max(s['startup_ms'] for s in samples)
    return {
        "avg_startup_ms": round(avg_startup, 2),
        "avg_reload_ms": round(avg_reload, 2),
        "peak_startup_ms": peak_startup,
    }

def detect_bottlenecks(summary):
    notes = []
    if summary['avg_startup_ms'] > 3500:
        notes.append('Cold start is high; review plugin count and transpilation scope.')
    if summary['avg_reload_ms'] > 1600:
        notes.append('Reload latency is elevated; inspect HMR asset invalidation size.')
    if summary['peak_startup_ms'] > 4500:
        notes.append('Large peak startup spikes; investigate antivirus/fs watcher pressure.')
    if not notes:
        notes.append('No critical bottlenecks detected in current sample.')
    return notes
