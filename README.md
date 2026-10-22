# Home — design reference

This is a design mockup created in a visual design tool, exported as a
standalone page. Treat it as a REFERENCE MOCKUP, not production code:
the markup and inline styles carry the design's precise values — colors,
font sizes, spacing, radii, shadows, layout — which an implementation
should replicate faithfully in its own components and styling system
rather than copy wholesale.

## Contents

- `index.html` (formerly Main.dc.html) — the home page artboard (a Design Component: an `<x-dc>`
  template + a small logic class). The values to replicate live in its
  inline `style="…"` attributes and the `<helmet><style>` block.
- `assets/` — files uploaded to the design (images, fonts, media)
- `support.js`, `vendor/react*.js` — the runtime that renders the
  component in a browser; not part of the design.

## Uploaded files

Images, fonts and media uploaded to the design are written once each under
`assets/` — 9 in this export — and the exported files refer to them there. A
reference a script puts together while the page runs (for example
`"/_blob/" + id`) is not rewritten and does not load from this folder.

## Viewing

Serve the folder (e.g. `python3 -m http.server`) and open `index.html`;
some browsers block the scripts over file://.

## Inner pages (added)

About, Leadership, Business, Investors, Auctions, Financials, Governance,
Ipo, Careers and Contact (`*.dc.html`) reuse the home page's styles, header
and footer, so they share one design system. Every nav, footer, breadcrumb
and anchor link resolves.

Grey `[bracketed]` text marks content still to be supplied: unconfirmed
dates, extra directors, auction notices 7 to 12, reserve prices and EMDs,
financial figures, committee members, policy status and the IPO terms.
PDF buttons point to `#` until the files are uploaded. The contact form
opens the visitor's email app (mailto) because no backend exists yet.

`_build/` holds the Python generator: run
`python3 _build/pages_a.py <site dir>` and `python3 _build/pages_b.py <site dir>`.
