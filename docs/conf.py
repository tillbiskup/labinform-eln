# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import subprocess

with open(os.path.join(os.path.dirname(__file__), '..', 'VERSION')) as \
        version_file:
    release_ = version_file.read().strip()

project = 'LabInform ELN'
copyright = '2019-2024, Mirjam Schröder; 2012–2024, Till Biskup'
author = 'Mirjam Schröder, Till Biskup'

# The short X.Y version
version = ".".join(release_.split('.')[0:2])
# The full version, including alpha/beta/rc tags
release = release_

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.todo',
    #    'sphinx_multiversion',
#    'sphinxcontrib.bibtex',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = './logo.png'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = './labinform-favicon.ico'

html_last_updated_fmt = '%Y-%m-%d'

numfig = True

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_link_only = True
