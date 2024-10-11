from typing import Any # pragma: no cover

src_contents = 'print("Hello, World!")\n' # pragma: no cover
fast = False # pragma: no cover
format_ipynb_string = lambda contents, fast, mode: contents # pragma: no cover
format_str = lambda contents, mode: contents.replace('\t', '    ') # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover
class MockMode:# pragma: no cover
    def __init__(self, preview: bool, is_ipynb: bool) -> None:# pragma: no cover
        self.preview = preview# pragma: no cover
        self.is_ipynb = is_ipynb# pragma: no cover
# pragma: no cover
mode = MockMode(preview=False, is_ipynb=False) # pragma: no cover
check_stability_and_equivalence = lambda src, dst, mode: None # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
src_contents = 'print(\"Hello, World!\")\n' # pragma: no cover
fast = False # pragma: no cover
def format_ipynb_string(contents, fast, mode): return contents.strip() # pragma: no cover
def format_str(contents, mode): return contents.strip() # pragma: no cover
class Mode:# pragma: no cover
    def __init__(self, preview, is_ipynb):# pragma: no cover
        self.preview = preview# pragma: no cover
        self.is_ipynb = is_ipynb # pragma: no cover
mode = Mode(preview=False, is_ipynb=False) # pragma: no cover
def check_stability_and_equivalence(src, dst, mode): return None # pragma: no cover

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
