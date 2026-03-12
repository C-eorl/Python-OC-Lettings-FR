# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# Ajouter le chemin du projet au PYTHONPATH pour importer les modules Django
sys.path.insert(0, os.path.abspath('..'))

# Configuration de Django pour permettre à Sphinx d'importer les modèles
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OC Lettings'
copyright = '2025, Orange County Lettings'
author = 'Orange County Lettings Team'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # Génération automatique de doc depuis docstrings
    'sphinx.ext.viewcode',      # Liens vers le code source
    'sphinx.ext.napoleon',      # Support Google/NumPy docstring style
    'sphinx.ext.githubpages',   # Support GitHub Pages
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Logo et favicon (optionnel)
# html_logo = '_static/logo.png'
# html_favicon = '_static/favicon.ico'

# Configuration du thème Read the Docs
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Support du Markdown (optionnel)
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.md': 'markdown',
# }