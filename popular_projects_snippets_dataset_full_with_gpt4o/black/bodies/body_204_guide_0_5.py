import logging # pragma: no cover
from difflib import unified_diff # pragma: no cover

def _format_str_once(string, mode): # pragma: no cover
    # For demonstration, let's simply return the input string reversed to create a difference # pragma: no cover
    return string[::-1] # pragma: no cover
 # pragma: no cover
def diff(a, b, fromfile, tofile): # pragma: no cover
    return '\n'.join(unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
 # pragma: no cover
def dump_to_file(mode, *diffs): # pragma: no cover
    log_filename = 'diff.log' # pragma: no cover
    with open(log_filename, 'w') as log_file: # pragma: no cover
        log_file.write(mode + '\n') # pragma: no cover
        for diff in diffs: # pragma: no cover
            log_file.write(diff + '\n') # pragma: no cover
    return log_filename # pragma: no cover
 # pragma: no cover
logging.basicConfig(level=logging.DEBUG) # pragma: no cover
src = 'print("Hello, world!")' # pragma: no cover
dst = 'print("Hello, world!")  ' # pragma: no cover
mode = 'example_mode' # pragma: no cover

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
