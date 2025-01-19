# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('./ldlm/py/py-ldlm/ldlm'))

project = 'LDLM'
copyright = '2024, Google LLC'
author = 'Ian Moore'
release = os.getenv("READTHEDOCS_VERSION_NAME", "latest")


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = []
exclude_patterns = ["py/.venv/*", "py/py-ldlm/*"]

# sphinxcontrib-osexample
extensions = [
	'multiproject',
	'myst_parser',
	'sphinx_tabs.tabs',
	'sphinx_copybutton',
	'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
]

autodoc_default_options = {
    'member-order': 'bysource',
}

autoclass_content = "both"
autosectionlabel_prefix_document = True

multiproject_projects = {
    "ldlm": {
        "use_config_file": False,
        "config": {
            "project": "LDLM",
            "html_title": "LDLM - Lightweight Distributed Lock Manager",
        },
    },
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
html_favicon = './images/favicon.ico'
