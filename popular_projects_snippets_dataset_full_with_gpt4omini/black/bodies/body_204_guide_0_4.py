from typing import Any, Dict # pragma: no cover
import difflib # pragma: no cover

src = 'print("Hello, World!")' # pragma: no cover
dst = 'print("Hello, World!\n")' # pragma: no cover
mode = 'format' # pragma: no cover
def _format_str_once(s: str, mode: str) -> str: return s + '\n' # pragma: no cover
def dump_to_file(mode: str, src_diff: str, dst_diff: str) -> str: return f'dump: mode={mode}, src_diff={src_diff}, dst_diff={dst_diff}' # pragma: no cover
def diff(a: str, b: str, name_a: str, name_b: str) -> str: return difflib.ndiff(a.splitlines(keepends=True), b.splitlines(keepends=True)) # pragma: no cover
class Mock: pass # pragma: no cover

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
