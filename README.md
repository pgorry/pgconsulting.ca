# pgconsulting.ca

Static rebuild of www.pgconsulting.ca (previously on Strikingly), hosted on GitHub Pages.
Plain HTML/CSS/JS — no framework, no build step on the server.

## Layout

- `index.html` — the one-page home site
- `blog/<slug>.html` — the nine case studies (served at `/blog/<slug>`, same URLs as Strikingly)
- `assets/site.css`, `assets/site.js` — styles; contact button + nav highlighting
- `assets/img/` — images pulled from the live Strikingly site
- `tools/build_posts.py` — regenerates `blog/*.html` from the post list inside it
- `CNAME` — tells GitHub Pages the custom domain

## Editing

- Home page: edit `index.html` directly.
- Case studies: edit the `POSTS` list in `tools/build_posts.py`, then run `python3 tools/build_posts.py` and commit the output.
- Contact address: built at click-time from character codes in `assets/site.js` so it never appears as text in the page or repo.

## Preview locally

```bash
python3 -m http.server 8000
```

(Extensionless `/blog/<slug>` links only resolve on GitHub Pages; locally open `/blog/<slug>.html`.)

## Deploy

1. Push to a public GitHub repo, then Settings → Pages → Deploy from branch → `main` / root.
2. DNS at GoDaddy (leave the Google MX records alone):
   - `www` CNAME → `<github-username>.github.io`
   - `@` A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Once the cert is issued, tick **Enforce HTTPS** in Settings → Pages.

## Fonts

Body text is Lato (same as before). Headings were Brandon Grotesque, an Adobe Fonts licence tied
to Strikingly; they now use Jost, the closest free match.
