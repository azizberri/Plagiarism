---
name: quant-trading-interview-prep
description: Plan what to study for quantitative trading (trader) interviews and online assessments - probability, expected value, mental math, market making, game theory, options basics. Use when asked to prep for quant trading interviews (Jane Street, Optiver, IMC, SIG, Citadel Securities, DRW, HRT), decide what to study or skip, scan uploaded course documents for coverage gaps, or recommend resources.
---

# Quant trading interview prep

Paths are relative to `.claude/skills/quant-trading-interview-prep/`. This is a research/planning skill, not an app, so it deviates from the `run-<unit>` naming of the generator template. The "driver" is `coverage.py`, which maps the user's course documents onto the topic taxonomy in `topics.json`.

## Workflow

1. **Clarify target** (ask only what is missing): role (trader vs researcher), firms, timeline, and the user's hours/week. Default to trader.
2. **Scan course documents** the user uploads (put them in one folder, e.g. `~/courses`):
   ```bash
   python3 coverage.py <docs_dir> --role trader --json coverage.json
   ```
   Reads txt/md/tex/py/ipynb/docx/pptx (stdlib) and pdf (needs `pdftotext`). Prints per topic: priority, `COVERED`/`PARTIAL`/`GAP`, and which files hit. Keyword hits show a topic *appears* in the material, not that the user has mastered it: skim the top files and check depth (does it include problems, or only definitions?). The `linear-algebra` keyword `matrix` also fires on "payoff/transition matrix", so treat that row as noisy.
3. **Refresh research** (formats change yearly; `references/firms.md` is dated 2026-10-15). Use WebSearch (works) for the target firms' current OA format, recent candidate reports and resources. WebFetch to firm and prep sites was blocked by the egress proxy in the authoring session (`403 CONNECT`); don't try to bypass it, rely on search snippets and say so, and ask the user to paste pages or YouTube transcripts they want analysed.
4. **Produce the plan** in this order, citing sources as links and labelling anything candidate-reported as such:
   - **Study** (core/high topics that are GAP/PARTIAL) with a recommended resource each.
   - **Already covered** (can skip or only light review) based on the scan.
   - **Don't study (yet)**: `low` priority topics for trader roles - stochastic calculus, ML/time series - unless the user targets research or a bank derivatives desk.
   - **Extra beyond courses**: mental-math drilling, market-making games, betting/Kelly, poker/game theory (SIG, DRW), options Greeks intuition, explaining reasoning aloud.
   - A week-by-week schedule sized to the user's timeline: mental math daily; probability/EV first; then games and market making; options and firm-specific last.
5. Offer to quiz the user (probability/EV questions, a live market-making game with you as counterparty).

## Priorities (summary of `topics.json`)

Core: mental arithmetic, probability, expected value, betting/EV games, market making. High: distributions, random walks/Markov/gambler's ruin, game theory, options basics. Medium: statistics, linear algebra/calculus, brainteasers, coding, market awareness. Low for traders: stochastic calculus, ML/time series.

## Gotchas

- Evidence quality is low-to-medium: nearly all of it is prep-site marketing or anonymous candidate reports. Say so; flag conflicts rather than picking one.
- Courses almost never cover mental math, market-making games or betting-game fluency, so expect these to show as GAP even for strong students.
- A broken or scanned (image-only) PDF yields no text and is counted as unreadable; ask for a text version or OCR it.
- Re-check `topics.json` keywords if the user's courses use different terminology (e.g. add a row rather than trusting a GAP).

## Resources and firm details

See `references/resources.md` (books, drills, communities) and `references/firms.md` (per-firm stages and weights).

## Verification record

Run in the authoring session: `coverage.py` on sample `.md/.txt/.tex/.docx` files (correct verdicts; corrupt PDF skipped with a count). Real `.pdf` and `.pptx` parsing paths were not exercised on real files. WebSearch research ran; WebFetch was blocked.
