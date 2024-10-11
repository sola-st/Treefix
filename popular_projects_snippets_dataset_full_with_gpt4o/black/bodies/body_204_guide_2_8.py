import difflib # pragma: no cover
import tempfile # pragma: no cover

src = 'def foo():\n    return 42' # pragma: no cover
dst = 'def foo():\n    return 42' # pragma: no cover
mode = type('MockMode', (object,), {'__str__': lambda self: 'mock_mode'})() # pragma: no cover
def _format_str_once(code, mode): # pragma: no cover
    return code + ' # reformatted' # pragma: no cover
def diff(a, b, fromfile, tofile): # pragma: no cover
    return '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
def dump_to_file(mode_str, diff1, diff2): # pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as f: # pragma: no cover
        f.write(f'Mode: {mode_str}\n\n{diff1}\n\n{diff2}') # pragma: no cover
        return f.name # pragma: no cover

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
