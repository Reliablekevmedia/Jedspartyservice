import { defineConfig } from 'astro/config';

// SITE_URL / SITE_BASE let the same code build for the real domain (default)
// and for the GitHub Pages preview at reliablekevmedia.github.io/Jedspartyservice/.
export default defineConfig({
  site: process.env.SITE_URL ?? 'https://www.jedspartyservices.com',
  base: process.env.SITE_BASE ?? '/',
});
