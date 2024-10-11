import difflib # pragma: no cover
import tempfile # pragma: no cover
import os # pragma: no cover

src = 'def foo():\n    return\n' # pragma: no cover
dst = 'def foo():\n    return None\n' # pragma: no cover
mode = type('Mode', (object,), {})() # pragma: no cover
def _format_str_once(code, mode): # pragma: no cover
    # Mocking the function to reformat the string # pragma: no cover
    return 'def foo():\n    return None\n' # pragma: no cover
def dump_to_file(mode_str, diff1, diff2): # pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.diff') as tmp: # pragma: no cover
        tmp.write(mode_str + '\n' + diff1 + '\n' + diff2) # pragma: no cover
        return tmp.name # pragma: no cover
def diff(original, modified, fromfile, tofile): # pragma: no cover
    return '\n'.join(difflib.unified_diff( # pragma: no cover
        original.splitlines(), # pragma: no cover
        modified.splitlines(), # pragma: no cover
        fromfile=fromfile, # pragma: no cover
        tofile=tofile, # pragma: no cover
        lineterm='' # pragma: no cover
    )) # pragma: no cover

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
