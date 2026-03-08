def analyze(samples):
    if not samples:
        return {'avg_cpu':0,'max_cpu':0,'avg_rss':0,'spikes':0}
    cpus=[s['cpu'] for s in samples]
    rss=[s['rss'] for s in samples]
    avg_cpu=sum(cpus)/len(cpus)
    max_cpu=max(cpus)
    avg_rss=sum(rss)/len(rss)
    spikes=sum(1 for c in cpus if c>80)
    return {'avg_cpu':round(avg_cpu,2),'max_cpu':round(max_cpu,2),'avg_rss':int(avg_rss),'spikes':spikes}
