def suggest(report):
    hints=[]
    if report.get('max_cpu',0) > 85:
        hints.append('CPU spikes detected: review hot-reload plugins and watcher scope.')
    if report.get('avg_rss',0) > 500*1024*1024:
        hints.append('High memory usage: reduce source maps or plugin load in dev mode.')
    if report.get('spikes',0) > 0:
        hints.append('Frequent spikes: debounce file watchers and exclude build artifacts.')
    if not hints:
        hints.append('No critical slowdown indicators found in sample window.')
    return hints
