# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Donald F. Ferguson Course and Projects'
copyright = 'Donald F. Ferguson, 2024.'
author = 'Donald F. Ferguson'
release = '0.3'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx extensions
extensions = [
    'myst_parser',
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "nbsphinx",
    "myst_parser",
    "jupyter_sphinx",
    "sphinx_design",
    "sphinx_jinja",
    # "ansys_sphinx_theme.extension.autoapi",
    "numpydoc",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'traditional'
html_static_path = ['_static']
# html_theme = 'sphinx_material'
html_theme = "ansys_sphinx_theme"
