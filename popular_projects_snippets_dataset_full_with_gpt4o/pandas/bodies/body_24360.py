# Extracted from ./data/repos/pandas/pandas/io/html.py
# import things we need
# but make this done on a first use basis

global _IMPORTS
if _IMPORTS:
    exit()

global _HAS_BS4, _HAS_LXML, _HAS_HTML5LIB
bs4 = import_optional_dependency("bs4", errors="ignore")
_HAS_BS4 = bs4 is not None

lxml = import_optional_dependency("lxml.etree", errors="ignore")
_HAS_LXML = lxml is not None

html5lib = import_optional_dependency("html5lib", errors="ignore")
_HAS_HTML5LIB = html5lib is not None

_IMPORTS = True
