from difflib import unified_diff # pragma: no cover
import logging # pragma: no cover

def _format_str_once(dst, mode): return dst + ' formatted once' # pragma: no cover
dst = 'original code block' # pragma: no cover
mode = 'default' # pragma: no cover
def dump_to_file(mode, src_diff, dst_diff): return 'log.txt' # pragma: no cover
def diff(a, b, label_a, label_b): return list(unified_diff(a.splitlines(), b.splitlines(), fromfile=label_a, tofile=label_b)) # pragma: no cover
src = 'original code block' # pragma: no cover

from difflib import unified_diff # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(dst: str, mode: str) -> str: return dst + ' formatted' # pragma: no cover
dst = 'def example_function():\n    return 42' # pragma: no cover
mode = 'example_mode' # pragma: no cover
def dump_to_file(mode: str, src_diff: str, dst_diff: str) -> str:# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:# pragma: no cover
        f.write(f'Mode: {mode}\nSrc Diff: {src_diff}\nDst Diff: {dst_diff}')# pragma: no cover
        return f.name # pragma: no cover
def diff(a: str, b: str, label_a: str, label_b: str) -> str:# pragma: no cover
    return '\n'.join(unified_diff(a.splitlines(), b.splitlines(), fromfile=label_a, tofile=label_b)) # pragma: no cover
src = 'def example_function():\n    return 0' # pragma: no cover

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
