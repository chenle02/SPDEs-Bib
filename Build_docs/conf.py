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
html_theme_options = {
    "footer": "Le Chen (陈乐), Auburn University, le.chen@auburn.edu, chenle02@gmail.com"
}

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
