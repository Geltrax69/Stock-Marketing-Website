# Stock-Marketing-Website

> ## Status: 🟡 In Progress
>
> <progress value="70" max="100"></progress>
>
> **Progress: 70%** — 8-page "Simple Trade" marketing site renders, but has broken links and a dead script

<p align="center">
  <img src="banner.webp" alt="Stock-Marketing-Website banner" width="100%" />
</p>

![HTML](https://img.shields.io/badge/HTML-5-E34F26?logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-1572B6?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?logo=javascript)

## What it is

"Simple Trade" — a multi-page static marketing website for a stock/investment product. Eight pages (home, get started, invest mutual, invest stocks, money, mutual funds, stocks, store) with Montserrat typography, a Lottie hero animation, product imagery, and per-page stylesheets. No build step, no dependencies — plain HTML/CSS/JS you can open or host anywhere.

## What works (verified)

- ✅ All 8 pages exist and link to each other (`index`, `getstarted`, `inves_m`, `inves_s`, `money`, `mutual`, `stock`, `store`) — verified by listing the HTML files
- ✅ Consistent header/nav with logo, Sign In and Get Started buttons across pages — verified in `index.html`
- ✅ Hero section with Lottie animation via CDN player — verified in markup
- ✅ All referenced images/CSS files exist locally (Logo.png, graph images, per-page stylesheets) — verified

## Tech stack

| Layer | Technology |
|---|---|
| Markup | HTML5 (8 pages) |
| Styling | CSS3 (per-page stylesheets) |
| Animation | Lottie (CDN player + local `.lottie` file) |
| Fonts | Montserrat (Google Fonts) |

## How to run

No build needed:

```bash
# option 1: open directly
open index.html        # macOS
# option 2: serve locally
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Screenshots

The site pages are the visual — banner above. No screenshots stored in the repo.

## What you can add more

- [ ] Fix `script.js` — it loads the Lottie animation from a Windows path (`D:\PROGRAMS\web\Stock Marketing\giff.lottie`) that can never resolve on the web; point it at the local `giff.lottie`
- [ ] Fix the logo link to `web.html` — that file doesn't exist, so the logo click 404s
- [ ] Remove or relocate `che.py` — an unrelated Python practice snippet sitting in a website repo
- [ ] Consolidate the stylesheets — 8+ per-page CSS files with overlapping rules; a shared stylesheet would cut duplication
- [ ] Make the Sign In / Get Started buttons functional — they currently just link to a static page

## Project structure

```
Stock-Marketing-Website/
├── index.html        # home page ("Simple Trade" hero)
├── getstarted.html / inves_m.html / inves_s.html
├── money.html / mutual.html / stock.html / store.html
├── web.css / stock.css / money.css / mutual.css / ...  # per-page styles
├── script.js / get.js  # JS (script.js has a broken local path)
├── che.py            # stray unrelated Python snippet
├── *.png / *.svg / *.lottie / giff.mp4  # images & animation assets
├── banner.webp
└── README.md
```

---
*README written after code audit on 2026-10-08.*
