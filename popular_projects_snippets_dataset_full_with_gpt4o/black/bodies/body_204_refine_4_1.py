import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(dst, mode=None):# pragma: no cover
    return dst.upper() if mode == 'uppercase' else dst.lower() # pragma: no cover
dst = 'example string' # pragma: no cover
mode = 'uppercase' # pragma: no cover
def dump_to_file(mode_str, diff1, diff2):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as f:# pragma: no cover
        f.write(mode_str + '\n')# pragma: no cover
        f.write(diff1 + '\n')# pragma: no cover
        f.write(diff2 + '\n')# pragma: no cover
        return f.name # pragma: no cover
def diff(original, modified, from_file, to_file):# pragma: no cover
    return '\n'.join(list(difflib.unified_diff(original.splitlines(), modified.splitlines(), fromfile=from_file, tofile=to_file))) # pragma: no cover
src = 'this is an example source' # pragma: no cover

import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(dst, mode=None):# pragma: no cover
    return dst if mode == 'NO_CHANGE' else dst[::-1] # pragma: no cover
dst = 'example string' # pragma: no cover
mode = 'NO_CHANGE' # pragma: no cover
def dump_to_file(mode_str, diff1, diff2):# pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as f:# pragma: no cover
        f.write(f'{mode_str}\n{diff1}\n{diff2}\n')# pragma: no cover
        return f.name # pragma: no cover
def diff(original, modified, from_file, to_file):# pragma: no cover
    return '\n'.join(list(difflib.unified_diff(original.splitlines(), modified.splitlines(), fromfile=from_file, tofile=to_file))) # pragma: no cover
src = 'example string' # pragma: no cover

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
