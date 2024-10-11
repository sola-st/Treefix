import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(s, mode):# pragma: no cover
    return s.upper() if mode == 'upper' else s.lower() # pragma: no cover
dst = 'Example string.' # pragma: no cover
mode = 'upper' # pragma: no cover
def dump_to_file(mode, diff1, diff2):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False) as temp:# pragma: no cover
        temp.write(f"Mode: {mode}\n\n".encode())# pragma: no cover
        temp.write(f"Diff 1:\n{diff1}\n\n".encode())# pragma: no cover
        temp.write(f"Diff 2:\n{diff2}".encode())# pragma: no cover
        return temp.name # pragma: no cover
def diff(a, b, fromfile, tofile):# pragma: no cover
    return '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
src = 'Original example string.' # pragma: no cover

import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(s, mode):# pragma: no cover
    return s if mode == 'DEFAULT' else s[::-1] # pragma: no cover
dst = 'example' # pragma: no cover
mode = 'DEFAULT' # pragma: no cover
def dump_to_file(mode, diff1, diff2):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp:# pragma: no cover
        temp.write(f"Mode: {mode}\n\n")# pragma: no cover
        temp.write(f"Diff 1:\n{diff1}\n\n")# pragma: no cover
        temp.write(f"Diff 2:\n{diff2}")# pragma: no cover
        temp_name = temp.name# pragma: no cover
    return temp_name # pragma: no cover
def diff(a, b, fromfile, tofile):# pragma: no cover
    return '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
src = 'example' # pragma: no cover

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
