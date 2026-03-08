# Dev Server Slowdown Profiler

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

Profile and explain local dev server slowdowns in real time.

## Usage
```bash
python3 main.py trace --pid 12345 --out samples/trace.json --seconds 3
python3 main.py report --trace samples/trace.json
python3 main.py report --trace samples/trace.json --json
```

## Sponsorware
Personal use is free. Team templates and advanced profiler packs require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
