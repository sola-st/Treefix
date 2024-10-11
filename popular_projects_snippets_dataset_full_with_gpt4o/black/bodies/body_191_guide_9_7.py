from types import SimpleNamespace # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
mode = SimpleNamespace(preview=False, is_ipynb=False) # pragma: no cover
# Ensure correct execution path # pragma: no cover
src_contents = 'Sample content' # pragma: no cover
# Non-empty to bypass the first NothingChanged exception # pragma: no cover
fast = False # pragma: no cover
# Set fast to False to trigger stability and equivalence checks # pragma: no cover
def format_ipynb_string(src_contents, fast, mode): return src_contents.upper() # pragma: no cover
# Placeholder function for format_ipynb_string # pragma: no cover
def format_str(src_contents, mode): return 'Formatted content' # pragma: no cover
# Change content to avoid src_contents == dst_contents and reach the uncovered path # pragma: no cover
def check_stability_and_equivalence(src_contents, dst_contents, mode): print('Stability and equivalence checked.') # pragma: no cover

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
