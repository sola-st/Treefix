import json # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
src_contents = 'print("Hello, World!")\n' # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover

import json # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
src_contents = '[{"cell_type": "code", "source": ["print(\"Hello, World!\n\")"]}]\n' # pragma: no cover
NothingChanged = NothingChanged # pragma: no cover
fast = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Format Jupyter notebook.

    Operate cell-by-cell, only on code cells, only for Python notebooks.
    If the ``.ipynb`` originally had a trailing newline, it'll be preserved.
    """
if mode.preview and not src_contents:
    _l_(5464)

    raise NothingChanged
    _l_(5463)

trailing_newline = src_contents[-1] == "\n"
_l_(5465)
modified = False
_l_(5466)
nb = json.loads(src_contents)
_l_(5467)
validate_metadata(nb)
_l_(5468)
for cell in nb["cells"]:
    _l_(5477)

    if cell.get("cell_type", None) == "code":
        _l_(5476)

        try:
            _l_(5475)

            src = "".join(cell["source"])
            _l_(5469)
            dst = format_cell(src, fast=fast, mode=mode)
            _l_(5470)
        except NothingChanged:
            _l_(5472)

            pass
            _l_(5471)
        else:
            cell["source"] = dst.splitlines(keepends=True)
            _l_(5473)
            modified = True
            _l_(5474)
if modified:
    _l_(5483)

    dst_contents = json.dumps(nb, indent=1, ensure_ascii=False)
    _l_(5478)
    if trailing_newline:
        _l_(5480)

        dst_contents = dst_contents + "\n"
        _l_(5479)
    aux = dst_contents
    _l_(5481)
    exit(aux)
else:
    raise NothingChanged
    _l_(5482)
