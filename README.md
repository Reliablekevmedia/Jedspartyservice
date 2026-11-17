# Jed's Party Services: website

The website for Jed's Party Services, built with [Astro](https://astro.build) and hosted on
GitHub Pages. The site itself lives in [`website/`](website/); see
[`website/README.md`](website/README.md) for how to run it, where things live and how to edit content.

## Editing the basics

Business name, phone, email, hours, menu, rates and staffing ratios are all in
`website/src/site.ts`. Change them there and every page updates.

## Hosting

- `.github/workflows/website.yml` builds the site and publishes it with GitHub Pages on every push
  to the default branch (one-time setup: **Settings → Pages → Source: GitHub Actions**).
- The address comes from GitHub Pages: `<account>.github.io/Jedspartyservice/` today, or the
  custom domain once one is added. Demo builds are hidden from search engines.
- `netlify.toml` is kept so the same project can also be hosted on Netlify if ever needed.

## Going live on jedspartyservices.com

1. In the repository: **Settings → Pages → Custom domain** → `www.jedspartyservices.com`, then add
   the DNS records GitHub shows at the domain registrar and tick **Enforce HTTPS**.
2. In `.github/workflows/website.yml`, delete the `PUBLIC_PREVIEW: "true"` line so Google can
   index the site.
3. Confirm the bar-top partners' names in `website/src/site.ts` (`barTopPartners`).

## Tools

- `tools/grade_photo.py`: gives new photos the site's warm, matte color grade
  (`python3 tools/grade_photo.py input.jpg website/public/img/output.jpg 1600`, add `0,0,1,1 mono` for black & white)
- `tools/wood_texture.py`: regenerates the walnut and oak wood textures (`numpy` + `Pillow`)
