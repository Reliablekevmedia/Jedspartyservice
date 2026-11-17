// Proportions of the traced logo pieces (viewBox width/height), used to size them in CSS and markup.
export const LOGO = {
  glass: { w: 108.38, h: 76.40 },
  jeds: { w: 403.97, h: 181.93 }, // "JED'S" with the martini-glass apostrophe; cap height = 123
  sub: { w: 424.49, h: 38.09 }, // "PARTY SERVICES"; cap height = 36
  full: { w: 470.26, h: 283.76 }, // the complete framed logo
};

export const glassViewBox = `0 0 ${LOGO.glass.w} ${LOGO.glass.h}`;
