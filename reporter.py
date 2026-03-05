import json

def print_profile(label, summary, bottlenecks, recs, as_json=False):
    payload = {
        "label": label,
        "summary": summary,
        "bottlenecks": bottlenecks,
        "recommendations": recs,
    }
    if as_json:
        print(json.dumps(payload, indent=2)); return
    print(f"Profile: {label}")
    print(f"Avg startup: {summary['avg_startup_ms']} ms")
    print(f"Avg reload: {summary['avg_reload_ms']} ms")
    print(f"Peak startup: {summary['peak_startup_ms']} ms")
    print('\nBottlenecks:')
    for b in bottlenecks:
        print(f"- {b}")
    print('\nRecommendations:')
    for r in recs:
        print(f"- {r}")
