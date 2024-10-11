import json # pragma: no cover

mode = type('Mock', (object,), {'preview': True})() # pragma: no cover
src_contents = '[]\n' # pragma: no cover
NothingChanged = Exception # pragma: no cover
def validate_metadata(nb):# pragma: no cover
    return True # pragma: no cover
def format_cell(src, fast, mode):# pragma: no cover
    return src # pragma: no cover
fast = True # pragma: no cover

import json # pragma: no cover

mode = type('Mock', (object,), {'preview': True})() # pragma: no cover
src_contents = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello World\")\n"]}]\n}' # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover
validate_metadata = lambda nb: None # pragma: no cover
format_cell = lambda src, fast, mode: src + '\n# formatted' # pragma: no cover
fast = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Format Jupyter notebook.

    Operate cell-by-cell, only on code cells, only for Python notebooks.
    If the ``.ipynb`` originally had a trailing newline, it'll be preserved.
    """
if mode.preview and not src_contents:
    _l_(17098)

    raise NothingChanged
    _l_(17097)

trailing_newline = src_contents[-1] == "\n"
_l_(17099)
modified = False
_l_(17100)
nb = json.loads(src_contents)
_l_(17101)
validate_metadata(nb)
_l_(17102)
for cell in nb["cells"]:
    _l_(17111)

    if cell.get("cell_type", None) == "code":
        _l_(17110)

        try:
            _l_(17109)

            src = "".join(cell["source"])
            _l_(17103)
            dst = format_cell(src, fast=fast, mode=mode)
            _l_(17104)
        except NothingChanged:
            _l_(17106)

            pass
            _l_(17105)
        else:
            cell["source"] = dst.splitlines(keepends=True)
            _l_(17107)
            modified = True
            _l_(17108)
if modified:
    _l_(17117)

    dst_contents = json.dumps(nb, indent=1, ensure_ascii=False)
    _l_(17112)
    if trailing_newline:
        _l_(17114)

        dst_contents = dst_contents + "\n"
        _l_(17113)
    aux = dst_contents
    _l_(17115)
    exit(aux)
else:
    raise NothingChanged
    _l_(17116)
