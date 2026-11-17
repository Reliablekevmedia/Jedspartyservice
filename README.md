# Jed's Party Services: Website Redesign

A static, dependency-free redesign of [jedspartyservices.com](https://www.jedspartyservices.com/).
The look is classy and understated: matte black, ivory and hand-finished wood, to echo the custom
bar tops Jed's serves from. The martini-glass apostrophe from the original logo carries the brand
throughout the site.

## Pages

| File | Content |
| --- | --- |
| `index.html` | Hero, mission, services overview, **The Craft** (custom bar tops), occasions, how it works, call to action |
| `services.html` | Bartender ($50/hr) and server ($40/hr) details, recommended staffing, interactive staffing & cost estimator |
| `about.html` | Jed Kessler's bio, personal philosophy, what to expect |
| `policies.html` | Free consultation, minimum hours, holidays, payment (25% / 75%), cancellation, office info |
| `contact.html` | Contact details and the Event Request Form (same fields as the original site) |

All content (rates, policies, bio, contact details, service area) comes from the current site.

## Design system

- **Colour:** matte ink `#141210`, ivory `#f5f1ea`, bone `#ece5da`, walnut `#4d3222`, oak `#a87b52` / `#c9a57d`.
  All tokens live at the top of `assets/css/styles.css`.
- **Type:** Cormorant Garamond (display; the bold weight is used for the logo) and Jost (body/labels),
  self-hosted in `assets/fonts` (SIL Open Font License).
- **Brand mark:** the logo is rebuilt in HTML/SVG: "JED" + martini-glass apostrophe + "S", with the
  framed variant (footer) where the glass breaks through the frame, as in the original logo.
  The martini glass also appears in section labels, dividers, list bullets, the favicon and as a faint watermark.
- **Craftsmanship motif:** a wood "bar top" ledge sits under every hero and above every call to action.
  Cards carry a thin oak inlay strip, and photos have offset oak frame lines.
- **Matte finish:** a very fine grain over the dark surfaces. Photos are colour-graded to a consistent warm,
  matte look: cool/purple stage lighting is muted and amber/wood tones are kept.

## Run it locally

No build step. Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Deploy

Upload the whole folder to any static host (Netlify, Vercel, GitHub Pages, Cloudflare Pages, or the
existing web host). Point the `jedspartyservices.com` domain at it.

**Netlify + GitHub (recommended):** in Netlify choose *Add new site → Import an existing project →
GitHub*, then pick this repository. `netlify.toml` already holds the settings (no build command, publish
the repository root), so leave the build fields empty. Every push to the deployed branch updates the
live site. `404.html` is Netlify's "page not found" page. The page names match the old Weebly site
(`/services.html`, `/about.html`, `/policies.html`, `/contact.html`), so existing links keep working.

## Before launch

1. **Confirm the bar-top partners' names.** `index.html` (The Craft section) credits
   *Vinny Weberg Media & Vintage Events*. Check the spelling and how they'd like to be credited.
   Add links to their sites or Instagram if wanted.
2. **Event Request Form delivery.** The form validates the fields, then opens the visitor's email app
   with a pre-filled request to `jedspartyservices@gmail.com`. No server is required.
   For in-page submissions instead, point the form at a form service (e.g. Formspree or Netlify Forms)
   and remove the `data-request-form` handler in `assets/js/main.js`.
3. **Photos.** The site uses the photos from the current website, colour-graded. Newer, higher-resolution
   photos of the custom bars and events will lift the design further. The portrait and bartending shots
   are small (~400px). Run new photos through the same grade for consistency:

   ```bash
   python3 tools/grade_photo.py input.jpg assets/img/output.jpg 1600          # warm matte grade
   python3 tools/grade_photo.py input.jpg assets/img/output.jpg 1600 0,0,1,1 mono   # warm black & white
   ```

   `tools/wood_texture.py` regenerates the walnut/oak wood textures (`numpy` + `Pillow`).

## Structure

```
index.html  services.html  about.html  policies.html  contact.html
assets/
  css/styles.css     design tokens, components, responsive rules
  js/main.js         menu, scroll reveal, staffing estimator, request form
  fonts/             self-hosted woff2 + licences
  img/               graded photos, wood textures, favicon, social share image
tools/               photo grading and wood texture generators
```

The header, footer and icon sprite are repeated in each page. If you change one, update all five pages.
