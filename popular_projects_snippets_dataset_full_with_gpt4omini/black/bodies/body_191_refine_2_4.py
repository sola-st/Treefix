from typing import Any, Dict # pragma: no cover

class MockMode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.preview = False# pragma: no cover
        self.is_ipynb = False# pragma: no cover
# pragma: no cover
mode = MockMode() # pragma: no cover
src_contents = 'Some example source code.' # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover
def format_ipynb_string(src, fast, mode):# pragma: no cover
    return src.replace('example', 'formatted') # pragma: no cover
fast = False # pragma: no cover
def format_str(src, mode):# pragma: no cover
    return src.replace('example', 'formatted') # pragma: no cover
def check_stability_and_equivalence(src, dst, mode):# pragma: no cover
    assert src != dst, 'Contents are identical.' # pragma: no cover

from typing import Any # pragma: no cover

class MockMode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.preview = False# pragma: no cover
        self.is_ipynb = False# pragma: no cover
# pragma: no cover
mode = MockMode() # pragma: no cover
src_contents = 'def example_function():\n    print("Hello, World!")' # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover
def format_ipynb_string(src, fast, mode):# pragma: no cover
    return src.replace('example_function', 'formatted_example_function') # pragma: no cover
fast = False # pragma: no cover
def format_str(src, mode):# pragma: no cover
    return src.replace('example_function', 'formatted_example_function') # pragma: no cover
def check_stability_and_equivalence(src, dst, mode):# pragma: no cover
    if src == dst:# pragma: no cover
        raise NothingChanged() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Reformat contents of a file and return new contents.

    If `fast` is False, additionally confirm that the reformatted code is
    valid by calling :func:`assert_equivalent` and :func:`assert_stable` on it.
    `mode` is passed to :func:`format_str`.
    """
if not mode.preview and not src_contents.strip():
    _l_(4368)

    raise NothingChanged
    _l_(4367)

if mode.is_ipynb:
    _l_(4371)

    dst_contents = format_ipynb_string(src_contents, fast=fast, mode=mode)
    _l_(4369)
else:
    dst_contents = format_str(src_contents, mode=mode)
    _l_(4370)
if src_contents == dst_contents:
    _l_(4373)

    raise NothingChanged
    _l_(4372)

if not fast and not mode.is_ipynb:
    _l_(4375)

    # Jupyter notebooks will already have been checked above.
    check_stability_and_equivalence(src_contents, dst_contents, mode=mode)
    _l_(4374)
aux = dst_contents
_l_(4376)
exit(aux)
