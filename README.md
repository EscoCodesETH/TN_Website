[![Netlify Status](https://api.netlify.com/api/v1/badges/4802b4d8-eda9-457c-b5e9-e177ffeb7e66/deploy-status)](https://app.netlify.com/projects/truenumbers/deploys)

# UP³ product website

Two static product pages built by True Numbers:

- `/` — UP³ pay, personnel, reconciliation and travel platform
- `/stars` — STARS travel and reimbursement within UP³

The site uses HTML and shared CSS. It has no JavaScript runtime, framework, web fonts, build step or third-party requests. Native HTML details elements make the case walkthrough keyboard accessible. Product navigation stays visible at mobile widths.

## Preview and checks

Run from the repository root:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
python3 tests/check_site.py
```

Open `http://127.0.0.1:4173/` or `http://127.0.0.1:4173/stars`. Python redirects the directory route to `/stars/`; Netlify's `_redirects` serves `/stars` directly from `stars/index.html`. No install or build command is needed.

## Content and visuals

Both products are in development. No public demo URL was supplied or verified, so all demo buttons link directly to `mailto:info@truenumbers.tech`.

The interface visuals are **synthetic workflow illustrations, not actual product screenshots**. They are labeled beside each visual and in its accessible description. Replace them with verified captures when available; retain concise captions and synthetic data. New image assets should have descriptive alternative text, explicit dimensions, and lazy loading below the fold. The checks enforce a 250 kB per-image and 600 kB per-page media budget.

[Content evidence](docs/content-evidence.md) records the source basis and limitations. The site makes no pilot, government relationship, external integration, accreditation or production-deployment claim. Travel authorization, voucher filing, Finance comparison and payment remain distinct.

## Files

- `index.html` and `stars/index.html`: product content
- `styles.css`: responsive layout, interface illustrations and focus styles
- `assets/favicon.svg`: small local icon
- `_redirects`: existing Netlify host's clean STARS route
- `tests/check_site.py`: dependency-free content, link, accessibility structure and performance checks

The prior decorative photographs, partner logos and animation script were removed. Changes can be reversed through Git; no source data, backend or payment behavior is part of this website.
