import sys # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
mode = SimpleNamespace(preview=False, is_ipynb=False) # pragma: no cover
src_contents = '' # pragma: no cover
fast = False # pragma: no cover
def format_ipynb_string(src_contents, fast, mode): return src_contents + ' formatted' # pragma: no cover
def format_str(src_contents, mode): return src_contents + ' formatted' # pragma: no cover
def check_stability_and_equivalence(src_contents, dst_contents, mode): pass # pragma: no cover
sys.exit = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Reformat contents of a file and return new contents.

    If `fast` is False, additionally confirm that the reformatted code is
    valid by calling :func:`assert_equivalent` and :func:`assert_stable` on it.
    `mode` is passed to :func:`format_str`.
    """
if not mode.preview and not src_contents.strip():
    _l_(15901)

    raise NothingChanged
    _l_(15900)

if mode.is_ipynb:
    _l_(15904)

    dst_contents = format_ipynb_string(src_contents, fast=fast, mode=mode)
    _l_(15902)
else:
    dst_contents = format_str(src_contents, mode=mode)
    _l_(15903)
if src_contents == dst_contents:
    _l_(15906)

    raise NothingChanged
    _l_(15905)

if not fast and not mode.is_ipynb:
    _l_(15908)

    # Jupyter notebooks will already have been checked above.
    check_stability_and_equivalence(src_contents, dst_contents, mode=mode)
    _l_(15907)
aux = dst_contents
_l_(15909)
exit(aux)
