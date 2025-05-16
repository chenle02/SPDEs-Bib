# SPDEs-Bib Documentation Source (Build_docs)
=============================================

This directory contains the source files and build scripts for the Sphinx-based
documentation of the SPDEs-Bib project, a curated bibliography for stochastic
partial differential equations and related topics.

## Directory Layout

- **audio_files/**  
  Contains raw WAV files (`*.wav`) and scripts for generating and injecting
  audio “podcast” snippets into entry pages.  

  - `add_podcast.py`: Inserts HTML `<audio>` players and download links into generated
    entry `.rst` files.  
  - `script.sh`: Bash helper for running external workflows (e.g., `nlm_workflow.sh`)
    to produce audio files.  
- **bib_entries/**  
  Auto-generated reStructuredText (`.rst`) files for individual BibTeX entries.  
- **bib_files/**  
  Auto-generated `.bib` files—one per entry—from the main `All.bib`.  
- **_static/**  
  Static assets (CSS, JS, images) used by the HTML theme.  
- **_templates/**  
  Custom Jinja2 templates for overriding Sphinx defaults.  
- **Root files**:
  - `conf.py`: Sphinx configuration.
  - `index.rst`: Main toctree entry point.
  - `Introduction.rst`, `By-Cite-Keys.rst`, `Contact.rst`, etc.: Documentation sections.
  - `Makefile` / `make.bat`: Build automation scripts.
  - `requirements.txt`: Python dependencies for building docs.

## Key Scripts

### 1. `Bibtexparser-all.py`
- Parses the master `All.bib` file and generates:
  - Individual `.bib` files in `bib_files/` (one per entry).
  - Entry pages in `bib_entries/` with citation blocks and raw BibTeX.
  - `By-Cite-Keys.rst`: an index listing all entries by citation key.
- Supports a `--fast` mode to skip regeneration of existing files.

### 2. `add_podcast.py` (in `audio_files/`)
- Scans each entry `.rst` in `bib_entries/` for a BibTeX code block.
- Injects an HTML `<audio>` player (`.. raw:: html`) and a “Download audio” link.

### 3. `script.sh` (in `audio_files/`)
- Bash script illustrating a pipeline using `nlm_workflow.sh` to convert PDFs/TXT to WAV audio.

## Sphinx Configuration (`conf.py`)

- **Extensions**:
  - `sphinxcontrib.bibtex` for native BibTeX support.
- **Theme**:
  - `press` theme via `sphinx_press_theme`.
- **Paths**:
  - `templates_path = ["_templates"]`
  - `html_static_path = ["_static"]`
  - `html_extra_path = ["audio_files"]` (so audio files are copied into the final build).
- **Audio Hook**:
  - `run_add_podcast()` is connected to the `builder-inited` event to inject audio snippets
    after the HTML build completes.

## Build Commands

### Unix/macOS
```bash
# Enter this directory and install dependencies
cd Build_docs
pip install -r requirements.txt

# Build HTML
make html

# Check for broken links
make linkcheck

# Build & deploy to GitHub Pages
make html-and-deploy
```

### Windows
```bat
cd Build_docs
make.bat html
make.bat linkcheck
```

## Dependencies

- **Python packages** (from `requirements.txt`):
  - `sphinx>=7.2.6`
  - `sphinxcontrib-bibtex`
  - `sphinx_press_theme`
- **Optional tools**:
  - `bibtex-tidy` for formatting generated `.bib` files.
  - Any additional scripts used by `script.sh` / `nlm_workflow.sh`.

## Deployment

- **GitHub Pages**:
  - The `deploy` target in `Makefile` rsyncs `_build/html/` to the `GHPAGEDIR`,
    commits, and pushes updates.
- **Read the Docs**:
  - `.readthedocs.yaml` points at this config (`Build_docs/conf.py`) and installs
    `requirements.txt` under Ubuntu 22.04 with Python 3.12.
  - Builds automatically on each commit; hosted at https://spdes-bib.readthedocs.io/
