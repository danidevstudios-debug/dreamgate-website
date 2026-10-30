# DreamGate developer website

Public site for the DreamGate developer account: lists all apps, sells
their full source codes, and doubles as the Play listing's developer
website (which AdMob needs for app-ads.txt verification).

## Files

- `apps.json` — the single source of truth. One object per app.
- `template.html` — page design with a `__APPS_JSON__` placeholder.
- `build.py` — injects `apps.json` into the template → `index.html`
  (fully self-contained, works on any static host).
- `index.html` — the generated page. Never edit by hand; rebuild instead.
- `app-ads.txt` — AdMob verification line. Must be served at the site
  root (`<domain>/app-ads.txt`) once this domain is the Play listing's
  developer website.

## Add a new app (the auto-add mechanism, phase 1)

1. Add one object to `apps.json` (copy an existing app, change name,
   package, store URL, description, features, privacy URL, status).
2. Run `python3 build.py`.
3. Redeploy `index.html` + `app-ads.txt`.

That is the whole manual step. The page renders entirely from
`apps.json`, so no HTML editing is ever needed for a new app.

## Phase 2 (planned, not wired yet)

Full automation: a GitHub Action (or a hook on the cloud-build repos)
that appends the new app to `apps.json`, runs `build.py`, and redeploys
whenever a new app is released. Needs the hosting choice below first.

## Deployment options (as of 2026-10-29)

- **Vercel (recommended):** free `*.vercel.app` subdomain, serves root
  files (app-ads.txt works). Needs the Vercel connector connected
  (connect link shared with Yasir 2026-10-29), then deploy via
  `create_deployment` with these files.
- **GitHub Pages:** needs a NEW public repo for this site (public repos
  support Pages on the Free plan). Site source contains no app sources
  and no secrets, but repo visibility needs Yasir's OK.
- **Custom domain later:** any domain can be pointed at either host;
  update the Play listing website to match, then AdMob re-crawls
  (24 hours to 7 days for domain changes).

## Source-code sales (phase 1 rules)

- Listings say "Contact to buy" — no prices set yet, no payment gateway
  wired. Yasir sets prices and the payment route (bank transfer /
  Payoneer are the realistic Pakistan options for website sales).
- Source zips are NEVER committed to this site repo: they are delivered
  privately after payment. The buyer's own signing key is required —
  DreamGate upload keystores are never shared or sold.
- Buyer email for every button: yourdreamgate@gmail.com.
