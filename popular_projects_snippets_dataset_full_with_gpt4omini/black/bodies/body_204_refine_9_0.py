from typing import Callable, Any # pragma: no cover
import difflib # pragma: no cover

_format_str_once = lambda s, mode: s + ' formatted' # pragma: no cover
dst = 'original string' # pragma: no cover
mode = 'standard' # pragma: no cover
dump_to_file = lambda mode_str, *args: 'dumped_to_file_path' # pragma: no cover
diff = lambda a, b, label1, label2: difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=label1, tofile=label2) # pragma: no cover
src = 'source string' # pragma: no cover

from typing import Callable, Any # pragma: no cover
import difflib # pragma: no cover
import tempfile # pragma: no cover

_format_str_once = lambda s, mode: s.replace('original', 'formatted') # pragma: no cover
dst = 'original code' # pragma: no cover
mode = 'formatting' # pragma: no cover
def dump_to_file(mode_str, src_diff, dst_diff):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False) as f:# pragma: no cover
        f.write(f'Mode: {mode_str}\nSource Diff: {src_diff}\nDestination Diff: {dst_diff}'.encode())# pragma: no cover
        return f.name # pragma: no cover
def diff(a, b, label1, label2):# pragma: no cover
    return '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=label1, tofile=label2)) # pragma: no cover
src = 'original code' # pragma: no cover

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
