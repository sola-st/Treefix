import difflib # pragma: no cover

def _format_str_once(s, mode):# pragma: no cover
    # Mock implementation that changes formatting# pragma: no cover
    return s.replace('a', 'b') if 'a' in s else s # pragma: no cover
def dump_to_file(*args):# pragma: no cover
    # Mock implementation# pragma: no cover
    return 'mock_diff.log' # pragma: no cover
def diff(a, b, name_a, name_b):# pragma: no cover
    # Mock implementation of diff using difflib# pragma: no cover
    diff_generator = difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=name_a, tofile=name_b)# pragma: no cover
    return '\n'.join(diff_generator) # pragma: no cover
src = 'source code with a problem' # pragma: no cover
dst = 'source code with a problem' # pragma: no cover
mode = 'mock_mode' # pragma: no cover

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
