from typing import Any # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover

mode = type('Mock', (object,), {'preview': False, 'is_ipynb': False})() # pragma: no cover
src_contents = '' # pragma: no cover
fast = False # pragma: no cover
def format_ipynb_string(src: str, fast: bool, mode: Any) -> str: return '' # pragma: no cover
def format_str(src: str, mode: Any) -> str: return '' # pragma: no cover
def check_stability_and_equivalence(src: str, dst: str, mode: Any): pass # pragma: no cover

from typing import Any # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
def format_ipynb_string(src_contents: str, fast: bool, mode: Any) -> str: return 'formatted_ipynb_content' # pragma: no cover
def format_str(src_contents: str, mode: Any) -> str: return 'formatted_str_content' # pragma: no cover
def check_stability_and_equivalence(src_contents: str, dst_contents: str, mode: Any): pass # pragma: no cover
src_contents = 'some code content' # pragma: no cover
fast = False # pragma: no cover
mode = type('Mock', (object,), {'preview': False, 'is_ipynb': False})() # pragma: no cover

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
