import psutil, time, json
from pathlib import Path

def sample_process(pid, seconds=3, interval=0.5):
    p=psutil.Process(pid)
    out=[]
    end=time.time()+seconds
    while time.time()<end:
        out.append({
            'ts': time.time(),
            'cpu': p.cpu_percent(interval=None),
            'rss': p.memory_info().rss,
            'threads': p.num_threads()
        })
        time.sleep(interval)
    return out

def save_trace(path, samples):
    Path(path).write_text(json.dumps(samples, indent=2), encoding='utf-8')
