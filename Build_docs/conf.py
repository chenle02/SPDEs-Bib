# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SPDEs-Bib: A Bibliography for Stochastic Partial Differential Equations and Related Topics"
copyright = "2023, Le Chen (陈乐) @ Auburn"
author = "Le Chen (陈乐)"
# email = "le.chen@auburn.edu, chenle02@gmail.com"
# affiliation = (
#     "Department of Mathematics and Statistics, Auburn University, Alabama, USA"
# )

bibtex_bibfiles = ["../All.bib"]
bibtex_default_style = 'unsrt'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinxcontrib.bibtex"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
# html_theme = "press"
# html_theme = "nature"
# html_theme = "pyramid"
html_theme = "press"

html_static_path = ["_static"]
html_extra_path = ["audio_files"]
html_baseurl = "https://chenle02.github.io/SPDEs-Bib/"
html_theme_options = {
    "footer": "Le Chen (陈乐), Auburn University, le.chen@auburn.edu, chenle02@gmail.com"
}

# Automatically inject audio podcast links after building docs
import subprocess
import os
import sys

def run_add_podcast(app):
    script_dir = os.path.join(os.path.dirname(__file__), 'audio_files')
    script_path = os.path.join(script_dir, 'add_podcast.py')
    if not os.path.exists(script_path):
        print(f"[audio] add_podcast.py not found at {script_path}")
        return
    print(f"[audio] Running add_podcast.py to inject audio into RST files")
    try:
        subprocess.run([sys.executable, script_path], cwd=script_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[audio] add_podcast.py failed: {e}")

def setup(app):
    app.connect('builder-inited', run_add_podcast)

# -- Options for latex pdf output -------------------------------------------------
# bibtex_bibfiles = ["../All-test.bib"]

title = "SPDEs-Bib"
subtitle = "A Bibliography for Stochastic Partial Differential Equations and Related Topics"

latex_engine = "xelatex"  # or 'lualatex'
latex_elements = {
    "preamble": f"""
    \\usepackage{{xeCJK}}
    \\setCJKmainfont{{Noto Sans CJK SC}}
    \\usepackage{{titling}}
    \\pretitle{{\\begin{{center}}\\Huge\\bfseries}}
    \\posttitle{{\\par\\end{{center}}\\vskip 0.5em}}
    \\preauthor{{\\begin{{center}}\\large\\lineskip 0.5em%
                \\begin{{tabular}}[t]{{c}}}}
    \\postauthor{{\\end{{tabular}}\\par\\end{{center}}}}
    \\predate{{\\begin{{center}}\\large}}
    \\postdate{{\\par\\end{{center}}}}

    \\title{{{title} \\vskip 0.5em \\normalsize {subtitle}}}
    """
}
