from typing import Any, Optional # pragma: no cover

class MockMode:# pragma: no cover
    def __init__(self, preview: bool, is_ipynb: bool):# pragma: no cover
        self.preview = preview# pragma: no cover
        self.is_ipynb = is_ipynb# pragma: no cover
# pragma: no cover
mode = MockMode(preview=False, is_ipynb=False) # pragma: no cover
src_contents = 'Some initial content in the source file.' # pragma: no cover
class NothingChanged(Exception):# pragma: no cover
    pass # pragma: no cover
def format_ipynb_string(contents: str, fast: bool, mode: Any) -> str:# pragma: no cover
    return 'Formatted IPYNB content.' # pragma: no cover
fast = False # pragma: no cover
def format_str(contents: str, mode: Any) -> str:# pragma: no cover
    return 'Formatted string content.' # pragma: no cover
def check_stability_and_equivalence(src: str, dst: str, mode: Any) -> None:# pragma: no cover
    pass # pragma: no cover

from typing import Any # pragma: no cover

class MockMode:# pragma: no cover
    def __init__(self, preview: bool, is_ipynb: bool):# pragma: no cover
        self.preview = preview# pragma: no cover
        self.is_ipynb = is_ipynb# pragma: no cover
# pragma: no cover
mode = MockMode(preview=False, is_ipynb=False) # pragma: no cover
src_contents = 'Some initial content in the source file.' # pragma: no cover
class NothingChanged(Exception):# pragma: no cover
    pass # pragma: no cover
def format_ipynb_string(contents: str, fast: bool, mode: Any) -> str:# pragma: no cover
    return 'Formatted IPYNB content.' # pragma: no cover
fast = False # pragma: no cover
def format_str(contents: str, mode: Any) -> str:# pragma: no cover
    return 'Some reformatted content.' # pragma: no cover
def check_stability_and_equivalence(src: str, dst: str, mode: Any) -> None:# pragma: no cover
    pass # pragma: no cover

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
