import os
import sys

sys.path.insert(0, os.path.abspath("../foo"))

project = "foodemo30"
copyright = "2025, Jelsin Palomino"
author = "Jelsin Palomino"
release = "v0.1.1"

extensions_part1 = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
extensions_part2 = ["sphinx.ext.napoleon"]
extensions = extensions_part1 + extensions_part2

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
language = "es"
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
