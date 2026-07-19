# ⚠️ Legacy build scripts — DO NOT RUN

These Python scripts were used (originally via Antigravity) to **bulk-generate**
book and series pages early in the site's life. They are archived here because
**re-running any of them re-introduces bugs** into the live site. They are kept
only for reference/history.

## Why they're dangerous

Each generator clones an existing page as a template (mostly
`the-great-christmas-disaster-book-page.html`) and does find-and-replace on the
visible content. Known problems if re-run:

1. **Wrong hidden meta descriptions.** The scripts copy the template's `<head>`
   verbatim and never replace the `<meta name="description">` / `og:description`
   / JSON-LD `description`. So every generated page inherited *The Great Christmas
   Disaster's* "Olivia Denton… color-coded binder…" description (and every series
   page inherited the *Love Only* description). This was fixed across all 70 pages
   on **2026-07-19**; re-running a generator would undo that fix.
2. **"COMING SOON" button regression.** `build_book_pages.py` replaces the buy
   button with a **disabled "COMING SOON"** placeholder. Those books are now
   released with live "Buy on Amazon" links — re-running would revert them to dead
   buttons and hurt sales.
3. **`strip_overlays.py`** rewrites `index.html` to delete the homepage
   series-card title overlays (currently in use).
4. **`fix_stand_in.py`** is a spent one-off migration that bulk-rewrites every
   `*.html` file.

## Archived here

`build_book_pages.py`, `build_ccc_pages.py`, `build_kingsleys_pages.py`,
`build_kingsleys_short_stories.py`, `build_legacy_pages.py`,
`build_short_stories.py`, `build_wf_pages.py`, `build_wf_short_stories.py`,
`generate_ccc.py`, `fix_stand_in.py`, `strip_overlays.py`

(Pure image utilities — `copy_and_crop.py`, `crop_banner.py`, `overlay.py` — were
left in the repo root; they don't touch HTML and are safe.)

## The correct workflow now: add books one at a time

1. Copy an existing sibling book page in the same series; update the title, series
   number, cover `src`, Amazon link, the visible blurb, **and** the `<head>` meta
   description / og:description / JSON-LD description (all three) to match the book.
2. Add a `.book-card-link` card to the series page grid, in order.
3. Update `index.html`: the series card `book-count` badge, the "…and N more!"
   line, and (for a new upcoming release) the "What's Next" section.

If bulk generation is ever truly needed again, these scripts must first be fixed
to (a) regenerate the meta/og/JSON-LD description from each book's own blurb, and
(b) use real Amazon links instead of the "COMING SOON" placeholder.
