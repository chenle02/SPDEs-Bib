# Repository Guidelines

## Project Structure & Module Organization
- `All.bib` and `All.tex`: canonical bibliography and LaTeX demo.
- `Build_docs/`: Sphinx docs source and helpers
  - `Bibtexparser-all.py`: generates `By-Cite-Keys.rst` and per-entry pages.
  - `conf.py`, `index.rst`, `_static/`, `_templates/`.
  - `bib_entries/`, `bib_files/`, `_build/` (generated).
- `Demo/`, images, and assets (e.g., `SPDE-Logo.png`).

## Build, Test, and Development Commands
- Install docs deps: `pip install -r Build_docs/requirements.txt`.
- Generate entry pages (full/fast):
  - `cd Build_docs && python3 Bibtexparser-all.py`
  - `cd Build_docs && python3 Bibtexparser-all.py --fast` (skip regeneration of bib files).
- Build Sphinx HTML: `cd Build_docs && make html` (outputs to `Build_docs/_build/html/`).
- LaTeX demo (CI mirrors this):
  - `lualatex All.tex && biber All && lualatex All.tex && lualatex All.tex`.
- Optional formatting for BibTeX (if installed): `bibtex-tidy file.bib -m`.

## Coding Style & Naming Conventions
- Python: PEP 8, 4‑space indent; small, pure functions preferred.
- BibTeX cite keys: `last.last:YY:firstword` (e.g., `dalang:99:extending`).
- Keep BibTeX fields consistent; prefer `doi`, `url`, `mrnumber` when available.
- Markdown/RST: sentence‑case headings; wrap at ~100 chars.

## Testing Guidelines
- Docs build cleanly: `sphinx-build -b html Build_docs Build_docs/_build/html -W` (treat warnings as errors).
- Validate LaTeX compiles as above; ensure `All.pdf` updates.
- Spot‑check generated pages: open `Build_docs/_build/html/By-Cite-Keys.html` and a few entries under `bib_entries/`.

## Commit & Pull Request Guidelines
- Use Conventional Commits when possible: `feat(docs): ...`, `chore(audio_files): ...`, `docs(bib_entries): ...`.
- PRs should include: purpose, sample cite keys changed/added, screenshots or paths to built pages, and links to related issues.
- Do not commit generated artifacts (`Build_docs/_build/`, PDFs). CI/maintainers handle deploys.

## Tips & Notes
- New entries should originate from MathSciNet when possible; keep IDs consistent.
- Prefer minimal changes per PR (easier review).
- Maintainers-only: `make -C Build_docs html-and-deploy` uses a local `GHPAGEDIR`; contributors should not run `deploy`.
