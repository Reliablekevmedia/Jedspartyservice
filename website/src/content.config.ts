import { defineCollection } from 'astro:content';
import { file } from 'astro/loaders';
import { z } from 'astro/zod';

// The service area: Northern New Jersey, county by county.
const counties = defineCollection({
  loader: file('src/data/counties.json'),
  schema: z.object({
    name: z.string(),
    order: z.number(),
    blurb: z.string(),
  }),
});

export const collections = { counties };
