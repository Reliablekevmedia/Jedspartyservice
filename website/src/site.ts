// One place for business details. Change them here and every page updates.
export const SITE = {
  name: "Jed's Party Services",
  tagline: 'Professional Party & Event Staffing',
  motto: 'Going the extra mile leaves a lifelong impression.',
  description:
    "Jed's Party Services provides professional bartenders, servers and event coordination for weddings, milestones and parties across Northern New Jersey.",
  owner: 'Jed Kessler',
  phone: '201.538.7276',
  phoneTel: '+12015387276',
  email: 'jedspartyservices@gmail.com',
  city: 'Fair Lawn',
  state: 'NJ',
  zip: '07410',
  hours: 'Available 24 hours',
  // TODO: confirm spelling and how the bar-top builders want to be credited.
  barTopPartners: 'Vinny Weberg Media & Vintage Events',
};

// Rates and staffing ratios. The services page, estimator and policies all read these.
export const RATES = {
  bartender: 50, // per hour, per bartender
  server: 40, // per hour, per server
  minHours: 4,
  guestsPerServer: [15, 25],
  guestsPerBartender: [30, 50],
  coordinatorAtStaff: 6, // recommend an event coordinator at this many staff
  depositPercent: 25,
  balanceDueHours: 72,
};

export const NAV = [
  { href: '/services', label: 'Services' },
  { href: '/#craft', label: 'The Craft' },
  { href: '/about', label: 'About' },
  { href: '/policies', label: 'Policies' },
  { href: '/contact', label: 'Contact' },
];
