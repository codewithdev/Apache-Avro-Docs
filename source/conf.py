# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'avro-docs'
copyright = '2022, Dev Prakash Sharma'
author = 'Dev Prakash Sharma'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx.ext.duration", "sphinx.ext.autosectionlabel",]

templates_path = ['_templates']
html_theme = 'furo'
exclude_patterns = []
html_theme_options = {
  "collapse_navigation": True,
  "navigation_depth": 2
}
myst_heading_anchors = 3

html_theme = 'press'
html_static_path = ['_static']
