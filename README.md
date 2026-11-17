# Jed's Party Services: website

The website for Jed's Party Services, built with [Astro](https://astro.build) and hosted on
[Netlify](https://www.netlify.com). The site itself lives in [`website/`](website/); see
[`website/README.md`](website/README.md) for how to run it, where things live and how to edit content.

## Editing the basics

Business name, phone, email, hours, menu, rates and staffing ratios are all in
`website/src/site.ts`. Change them there and every page updates.

## Hosting

- `netlify.toml` holds the hosting settings: Netlify builds `website/` and publishes `website/dist`.
- Demo address: `jedspartyservices.netlify.app` (hidden from search engines during the demo phase).
- Old Weebly addresses (`/services.html`, `/about.html`, …) redirect to the new pages.

## Going live on jedspartyservices.com

1. In Netlify: **Domain management → Add a domain** → `jedspartyservices.com`, then add the DNS
   records Netlify shows at the domain registrar.
2. In `netlify.toml`, delete the `PUBLIC_PREVIEW = "true"` line so Google can index the site.
3. Confirm the bar-top partners' names in `website/src/site.ts` (`barTopPartners`).

## Tools

- `tools/grade_photo.py`: gives new photos the site's warm, matte color grade
  (`python3 tools/grade_photo.py input.jpg website/public/img/output.jpg 1600`, add `0,0,1,1 mono` for black & white)
- `tools/wood_texture.py`: regenerates the walnut and oak wood textures (`numpy` + `Pillow`)
