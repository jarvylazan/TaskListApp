
import os
import sys
sys.path.insert(0, os.path.abspath('../../app'))

project = 'Task List App'
copyright = '2025'
author = 'Your Name'
release = '1.0'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
