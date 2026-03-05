# Dev Server Slowdown Profiler

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

CLI profiler for measuring local dev-server startup/reload performance and generating optimization suggestions.

## Usage
```bash
python3 main.py profile --iterations 5 --label before --out before.json
python3 main.py profile --iterations 5 --label after --out after.json
python3 main.py compare --before before.json --after after.json
python3 main.py suggest --session after.json
```

## Sponsorware
Personal evaluation is free. Commercial/team usage and advanced diagnostic adapters require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
