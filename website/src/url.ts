// Build a link or asset path that works wherever the site is hosted: at the domain root
// (jedspartyservices.com, Netlify) or in a subfolder (the GitHub Pages preview).
export const url = (path: string) => `${import.meta.env.BASE_URL.replace(/\/$/, '')}${path}`;
