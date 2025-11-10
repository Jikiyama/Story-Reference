# Story Reference Explorer

A stable, dependency-light dashboard to explore narrative references detected in annotated tweets/posts.

## Features
- Load JSON from file or URL (also via `?data=...` and optional `?title=...` query params)
- Leaflet world map with custom clustering by radius (miles)
- Timeline slider with Play (Day/Week/Month) sliding window
- Story-year filter slider with decade quick buttons
- Story and Actor multi-select filters (with search; All/None; Actors: Top 25)
- Charts (Chart.js): Top Stories, Top Actors, References over Time
- Export current filtered events to CSV
- Robust parsing of years, dates, and coordinates
- Dark theme, accessible controls, no external fonts

1) Install Node.js (first time only)
Windows

Go to the Node.js website and download the LTS installer.

Run it. Keep the defaults.

Close and reopen PowerShell or Command Prompt.

macOS

Easiest: download the LTS macOS installer and run it.

If you already have Homebrew: brew install node@20 then brew link --overwrite node@20



## Quick start
```bash
npm install
npm run dev
```
The dashboard should load on http://localhost:5173/ and you can submit the merged_output.normalized.json that is in the root directory.