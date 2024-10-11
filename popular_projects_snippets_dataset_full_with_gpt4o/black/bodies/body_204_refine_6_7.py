import tempfile # pragma: no cover
import difflib # pragma: no cover

_format_str_once = lambda s, mode: s[::-1] # pragma: no cover
dst = 'example_dst' # pragma: no cover
mode = 'example_mode' # pragma: no cover
dump_to_file = lambda *args: tempfile.mktemp() # pragma: no cover
diff = lambda a, b, desc1, desc2: '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=desc1, tofile=desc2)) # pragma: no cover
src = 'example_src' # pragma: no cover

import tempfile # pragma: no cover
import difflib # pragma: no cover

def _format_str_once(s, mode=None):# pragma: no cover
    return s.lower() # pragma: no cover
dst = 'example string' # pragma: no cover
mode = 'lowercase' # pragma: no cover
def dump_to_file(mode_str, diff1, diff2):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as f:# pragma: no cover
        f.write(mode_str + '\n')# pragma: no cover
        f.write(diff1 + '\n')# pragma: no cover
        f.write(diff2 + '\n')# pragma: no cover
        return f.name # pragma: no cover
def diff(original, modified, from_file, to_file):# pragma: no cover
    return '\n'.join(list(difflib.unified_diff(original.splitlines(), modified.splitlines(), fromfile=from_file, tofile=to_file))) # pragma: no cover
src = 'INITIAL STRING' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Raise AssertionError if `dst` reformats differently the second time."""
# We shouldn't call format_str() here, because that formats the string
# twice and may hide a bug where we bounce back and forth between two
# versions.
newdst = _format_str_once(dst, mode=mode)
_l_(16833)
if dst != newdst:
    _l_(16836)

    log = dump_to_file(
        str(mode),
        diff(src, dst, "source", "first pass"),
        diff(dst, newdst, "first pass", "second pass"),
    )
    _l_(16834)
    raise AssertionError(
        "INTERNAL ERROR: Black produced different code on the second pass of the"
        " formatter.  Please report a bug on https://github.com/psf/black/issues."
        f"  This diff might be helpful: {log}"
    ) from None
    _l_(16835)
