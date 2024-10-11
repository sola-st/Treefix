import difflib # pragma: no cover
import logging # pragma: no cover

def _format_str_once(code, mode=None): # pragma: no cover
    # This mock method will simulate a formatter that alters the string # pragma: no cover
    return code.replace('original', 'modified') # pragma: no cover
 # pragma: no cover
def diff(a, b, fromfile, tofile): # pragma: no cover
    diff_lines = difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile) # pragma: no cover
    return '\n'.join(diff_lines) # pragma: no cover
 # pragma: no cover
def dump_to_file(mode_str, *diffs): # pragma: no cover
    log_file = 'log.txt' # pragma: no cover
    with open(log_file, 'w') as file: # pragma: no cover
        file.write('Mode: ' + mode_str + '\n') # pragma: no cover
        for diff in diffs: # pragma: no cover
            file.write(diff + '\n') # pragma: no cover
    return log_file # pragma: no cover
 # pragma: no cover
src = 'original code line 1\noriginal code line 2' # pragma: no cover
dst = 'original code line 1\nmodified code line 2' # pragma: no cover
mode = type('Mode', (object,), {}) # pragma: no cover

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
