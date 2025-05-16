# Codex Project Instructions: SPDEs-Bib

## Objective

This Codex configuration is designed to assist in the maintenance and quality assurance of the [SPDEs-Bib](https://github.com/chenle02/SPDEs-Bib) repository, with a particular focus on its [Sphinx-generated documentation](https://spdes-bib.readthedocs.io/en/latest/), which is automatically built and hosted via Read the Docs.

Codex should support tasks such as:

* Verifying the integrity of the Sphinx configuration.
* Ensuring proper rendering of BibTeX entries.
* Maintaining the table of contents and intersphinx references.
* Detecting broken links and formatting inconsistencies.
* Validating BibTeX parsing and citation consistency.

---

## Repository Overview

* **Main repository**: [https://github.com/chenle02/SPDEs-Bib](https://github.com/chenle02/SPDEs-Bib)
* **Documentation homepage**: [https://spdes-bib.readthedocs.io/en/latest/](https://spdes-bib.readthedocs.io/en/latest/)
* **Sphinx configuration**: Located in the `Build_docs/` directory
* **Entry point**: `Build_docs/index.rst`
* **Build automation**: Handled by Read the Docs based on `.readthedocs.yaml`

---

## Codex Responsibilities

1. **Verify Documentation Configuration**

   * Check that `conf.py` includes necessary extensions (e.g., `sphinxcontrib.bibtex`).
   * Ensure `index.rst` and submodules are well-formed.

2. **Check BibTeX Rendering**

   * Confirm correct parsing of BibTeX entries.
   * Validate that citation keys render properly in reST content.

3. **Detect Link Issues**

   * Optionally run Sphinx link checks.
   * Report broken external or internal references.

4. **Update TOC and Structure**

   * Maintain correct `toctree` hierarchy in `index.rst`.
   * Flag orphaned `.rst` or `.md` files.

5. **Ensure Build Stability on Read the Docs**

   * Monitor Read the Docs build logs.
   * Highlight warnings or errors in builds.

6. **Enforce Content Guidelines**

   * Prefer `.rst` over `.md` unless Markdown support is explicitly configured.
   * All math expressions should use `.. math::` or `:math:` syntax.
   * Avoid scanning large auto-generated directories such as:

     * `Build_docs/bib_entries/`
     * `Build_docs/bib_files/`
     * `Build_docs/audio_files/*.wav`
   * When generating or editing files (e.g., `README.md`, scripts), **remove all trailing spaces** to maintain clean formatting.

---

## Project Structure (Key Paths)

Below is a simplified view of the relevant directory structure:

```
.
├── All.bib                  # Main BibTeX file
├── Build_docs/              # Sphinx documentation source
│   ├── conf.py              # Sphinx configuration file
│   ├── index.rst            # Main entry point for documentation
│   ├── README.md            # Explains documentation build system, scripts, and deployment
│   ├── *.rst                # Additional documentation sections
│   ├── bib_entries/         # Parsed bibliographic content (auto-generated, ~7000 files)
│   └── _static/, _templates/ # Sphinx assets
├── .readthedocs.yaml        # Configuration for Read the Docs
├── .codex/                  # Codex configuration and instructions
│   ├── config.yaml
│   └── Instructions.md
├── Demo/                    # Sample LaTeX/BibTeX documents
├── Readme.md                # Project overview
└── Sample_setup_using_neovim.md # Editor configuration example
```

> Note: All documentation build tasks should operate within `Build_docs/`, and bibliographic parsing centers around `All.bib`. The `bib_entries/` directory is auto-generated and contains thousands of files; avoid indexing it unless required.

---

## Notes

* This repository serves as a curated reference for stochastic partial differential equations.
* Contributions should follow established formatting and citation conventions.
* Codex should support maintainers in ensuring a clean and consistent documentation experience for public users.

For issues, questions, or contributions, contact the maintainer at [chenle02@gmail.com](mailto:chenle02@gmail.com).
