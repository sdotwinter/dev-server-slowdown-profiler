import argparse, json
from pathlib import Path
from runner import run_profile, save_session
from analyzer import summarize, detect_bottlenecks
from recommender import recommend
from reporter import print_profile

def _load_session(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def run(argv=None):
    p = argparse.ArgumentParser(prog='dev-server-slowdown-profiler', description='Profile local dev server slowdown.')
    sub = p.add_subparsers(dest='cmd', required=True)

    a = sub.add_parser('profile')
    a.add_argument('--iterations', type=int, default=5)
    a.add_argument('--label', default='current')
    a.add_argument('--out', default='profile-current.json')
    a.add_argument('--json', action='store_true')

    b = sub.add_parser('compare')
    b.add_argument('--before', required=True)
    b.add_argument('--after', required=True)

    c = sub.add_parser('suggest')
    c.add_argument('--session', required=True)
    c.add_argument('--json', action='store_true')

    args = p.parse_args(argv)

    if args.cmd == 'profile':
        samples = run_profile(iterations=args.iterations)
        save_session(Path(args.out), samples, args.label)
        s = summarize(samples)
        b = detect_bottlenecks(s)
        r = recommend(s, b)
        print_profile(args.label, s, b, r, as_json=args.json)
        return 0

    if args.cmd == 'compare':
        before = _load_session(Path(args.before))
        after = _load_session(Path(args.after))
        s1 = summarize(before.get('samples', []))
        s2 = summarize(after.get('samples', []))
        delta_start = round(s2['avg_startup_ms'] - s1['avg_startup_ms'], 2)
        delta_reload = round(s2['avg_reload_ms'] - s1['avg_reload_ms'], 2)
        print(f"Startup delta (after-before): {delta_start} ms")
        print(f"Reload delta (after-before): {delta_reload} ms")
        return 0

    if args.cmd == 'suggest':
        session = _load_session(Path(args.session))
        s = summarize(session.get('samples', []))
        b = detect_bottlenecks(s)
        r = recommend(s, b)
        print_profile(session.get('label', 'session'), s, b, r, as_json=args.json)
        return 0

    return 0
