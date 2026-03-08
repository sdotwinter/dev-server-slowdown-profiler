import argparse, json
from pathlib import Path
from collector import sample_process, save_trace
from analyzer import analyze
from hints import suggest

def run(argv=None):
    p=argparse.ArgumentParser(prog='dev-server-slowdown-profiler')
    sub=p.add_subparsers(dest='cmd', required=True)

    t=sub.add_parser('trace'); t.add_argument('--pid', type=int, required=True); t.add_argument('--out', required=True); t.add_argument('--seconds', type=int, default=3)
    s=sub.add_parser('sample'); s.add_argument('--pid', type=int, required=True); s.add_argument('--seconds', type=int, default=2)
    r=sub.add_parser('report'); r.add_argument('--trace', required=True); r.add_argument('--json', action='store_true')

    a=p.parse_args(argv)

    if a.cmd in ('trace','sample'):
        smp=sample_process(a.pid, seconds=a.seconds, interval=0.5)
        if a.cmd=='trace':
            save_trace(a.out, smp)
            print(f"Trace saved: {a.out} ({len(smp)} samples)")
        else:
            print(json.dumps(smp, indent=2))
        return 0

    data=json.loads(Path(a.trace).read_text(encoding='utf-8'))
    rep=analyze(data)
    h=suggest(rep)
    payload={'report':rep,'hints':h}
    if a.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"avg_cpu={rep['avg_cpu']} max_cpu={rep['max_cpu']} avg_rss={rep['avg_rss']} spikes={rep['spikes']}")
        for x in h: print(f"- {x}")
    return 0
