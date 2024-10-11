import difflib # pragma: no cover

_format_str_once = lambda s, mode: s.encode(mode).decode(mode) # pragma: no cover
dst = 'example code' # pragma: no cover
mode = 'utf-8' # pragma: no cover
dump_to_file = lambda *args: 'path/to/diff.log' # pragma: no cover
diff = lambda a, b, desc1, desc2: '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=desc1, tofile=desc2)) # pragma: no cover
src = 'original code' # pragma: no cover

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
