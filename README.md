# Uphill

Mobile-first walking log for incline walks: enter incline %, speed and time, and Uphill estimates calories (ACSM walking equation), tracks streaks and weekly WHO minutes, and rewards progress with achievements and points you can trade for self-set rewards.

- **Today** — a landscape where the sun rises with today's minutes and a walker climbs toward the next landmark (Baiyoke Tower II → Everest) as total elevation grows
- **Stats** — weekly progress ring, 12-week bars, 14-day chart, trends, calendar, fun facts
- **Rewards** — points, levels, achievements, custom rewards
- **History** — every walk with calories, intensity zone and grade

## Use it

Open **https://oldwennork.github.io/uphill/** on your phone, then add it to your home screen (Safari: Share → Add to Home Screen · Chrome: ⋮ → Add to Home screen). It opens full screen like an app. Walks are stored only on that device, in that browser.

## Files

- `index.html` — the app, written as a claude.ai artifact (inside claude.ai it syncs to your account)
- `docs/` — the GitHub Pages build: the same app plus manifest and home-screen icons
- `tools/build_pages.py` — regenerates `docs/` from `index.html` (`python3 tools/build_pages.py`, needs Pillow)
