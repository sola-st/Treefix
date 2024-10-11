import tempfile # pragma: no cover

_format_str_once = lambda dst, mode: dst.lower() # pragma: no cover
dst = 'SOME TEST STRING' # pragma: no cover
mode = 'test_mode' # pragma: no cover
dump_to_file = lambda mode, first_diff, second_diff: f"Dumped log with mode={mode}" # pragma: no cover
diff = lambda old, new, from_name, to_name: f"Diff from {from_name} to {to_name}" # pragma: no cover
src = 'Original Source Code' # pragma: no cover

import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(dst, mode=None):# pragma: no cover
    return dst.lower() # pragma: no cover
dst = 'some test string' # pragma: no cover
mode = 'lowercase_mode' # pragma: no cover
def dump_to_file(mode_str, diff1, diff2):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_file:# pragma: no cover
        temp_file.write(f"Mode: {mode_str}\n\n")# pragma: no cover
        temp_file.write(f"Diff 1:\n{diff1}\n\n")# pragma: no cover
        temp_file.write(f"Diff 2:\n{diff2}")# pragma: no cover
        return temp_file.name # pragma: no cover
def diff(before, after, fromfile, tofile):# pragma: no cover
    return '\n'.join(difflib.unified_diff(before.splitlines(), after.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
src = 'Original Test String' # pragma: no cover

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
