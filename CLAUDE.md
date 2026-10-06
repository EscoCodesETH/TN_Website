# Website development notes

This repository is the static UP³ product website developed by True Numbers. STARS is the named travel and reimbursement service within UP³.

Use two pages: `index.html` for `/` and `stars/index.html` for `/stars`. Shared styling lives in `styles.css`. No framework or build process is required. Preview with `python3 -m http.server 4173 --bind 127.0.0.1`; verify with `python3 tests/check_site.py`.

Keep navigation limited to UP³, STARS and the demo CTA. Use a small "Built by True Numbers" footer attribution. Do not add Company, About or Contact pages/sections, or forms. Demo CTAs use `mailto:info@truenumbers.dev` until a valid demo URL is supplied.

Preserve clear development status. Ground implemented-feature claims in product code and verified captures; label any planned feature. Current visuals are synthetic workflow illustrations, explicitly labeled as such. See `docs/content-evidence.md` for provenance. Keep authorization, voucher filing, Finance review and payment distinct.

Use system fonts, local assets, native HTML interactions and a calm blue palette. Avoid continuous animation, scroll handlers and decorative large media. Any product captures must use synthetic data, dimensions and below-fold lazy loading. Test both desktop and mobile layouts, keyboard navigation and readable contrast.
