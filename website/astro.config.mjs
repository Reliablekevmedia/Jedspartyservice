import { defineConfig } from 'astro/config';

// Netlify sets URL to the site's address. SITE_URL / SITE_BASE can override it,
// e.g. to host a copy in a subfolder.
export default defineConfig({
  // Netlify provides URL (its .netlify.app address now, jedspartyservices.com once connected).
  site: process.env.SITE_URL ?? process.env.URL ?? 'https://www.jedspartyservices.com',
  base: process.env.SITE_BASE ?? '/',
});
