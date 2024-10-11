from typing import Any, Callable # pragma: no cover
import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(dst: str, mode: str) -> str:# pragma: no cover
    return dst + ' formatted' # pragma: no cover
dst = 'original code' # pragma: no cover
mode = 'example_mode' # pragma: no cover
def dump_to_file(mode: str, first_diff: str, second_diff: str) -> str:# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False) as f:# pragma: no cover
        f.write(f'Mode: {mode}\nFirst Diff: {first_diff}\nSecond Diff: {second_diff}'.encode())# pragma: no cover
        return f.name # pragma: no cover
def diff(a: str, b: str, label1: str, label2: str) -> str:# pragma: no cover
    d = difflib.ndiff(a.splitlines(), b.splitlines())# pragma: no cover
    return '\n'.join(d) # pragma: no cover
src = 'source code' # pragma: no cover

from typing import Any, Callable # pragma: no cover
import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(dst: str, mode: str) -> str:# pragma: no cover
    return dst.replace('original', 'formatted') # pragma: no cover
dst = 'formatted code sample' # pragma: no cover
mode = 'default' # pragma: no cover
def dump_to_file(mode: str, first_diff: str, second_diff: str) -> str:# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False) as f:# pragma: no cover
        f.write(f'Mode: {mode}\nFirst Diff: {first_diff}\nSecond Diff: {second_diff}'.encode())# pragma: no cover
        return f.name # pragma: no cover
def diff(a: str, b: str, label1: str, label2: str) -> str:# pragma: no cover
    return '\n'.join(list(difflib.ndiff(a.splitlines(), b.splitlines()))) # pragma: no cover
src = 'formatted code sample' # pragma: no cover

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
