def recommend(summary, bottlenecks):
    recs = []
    if summary['avg_startup_ms'] > 3500:
        recs.append('Enable dependency pre-bundling and prune unused plugins.')
    if summary['avg_reload_ms'] > 1600:
        recs.append('Split hot paths and reduce invalidated module graph breadth.')
    if summary['peak_startup_ms'] > 4500:
        recs.append('Exclude heavy directories from watch mode and check disk IO load.')
    if not recs:
        recs.append('Baseline is healthy; capture before/after profile when changing tooling.')
    return recs
