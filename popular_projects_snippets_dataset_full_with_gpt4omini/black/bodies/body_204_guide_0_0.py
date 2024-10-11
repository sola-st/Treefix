from typing import Any, Dict # pragma: no cover
import difflib # pragma: no cover

mode = 'test_mode' # pragma: no cover
src = 'original code here' # pragma: no cover
dst = 'modified code here' # pragma: no cover
def _format_str_once(dst, mode): return dst + '\n# formatted' # pragma: no cover
def diff(first: str, second: str, label1: str, label2: str) -> str: return '\n'.join(difflib.unified_diff(first.splitlines(keepends=True), second.splitlines(keepends=True), fromfile=label1, tofile=label2)) # pragma: no cover
def dump_to_file(*args: Any) -> str: return 'logged diff' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Raise AssertionError if `dst` reformats differently the second time."""
# We shouldn't call format_str() here, because that formats the string
# twice and may hide a bug where we bounce back and forth between two
# versions.
newdst = _format_str_once(dst, mode=mode)
_l_(5043)
if dst != newdst:
    _l_(5046)

    log = dump_to_file(
        str(mode),
        diff(src, dst, "source", "first pass"),
        diff(dst, newdst, "first pass", "second pass"),
    )
    _l_(5044)
    raise AssertionError(
        "INTERNAL ERROR: Black produced different code on the second pass of the"
        " formatter.  Please report a bug on https://github.com/psf/black/issues."
        f"  This diff might be helpful: {log}"
    ) from None
    _l_(5045)
