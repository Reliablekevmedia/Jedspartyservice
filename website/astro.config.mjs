import { defineConfig } from 'astro/config';

// SITE_URL / SITE_BASE let the same code build for the real domain, the Netlify demo
// and the GitHub Pages preview at reliablekevmedia.github.io/Jedspartyservice/.
export default defineConfig({
  // Netlify provides URL (its .netlify.app address now, jedspartyservices.com once connected).
  site: process.env.SITE_URL ?? process.env.URL ?? 'https://www.jedspartyservices.com',
  base: process.env.SITE_BASE ?? '/',
});
