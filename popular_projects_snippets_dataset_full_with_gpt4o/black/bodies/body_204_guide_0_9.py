from difflib import unified_diff # pragma: no cover

src = "original code" # pragma: no cover
dst = "formatted code" # pragma: no cover
mode = type("Mode", (object,), {})() # pragma: no cover
_format_str_once = lambda dst, mode: dst + " updated" # pragma: no cover
def dump_to_file(*args): # pragma: no cover
    return "diff_log.txt" # pragma: no cover
def diff(a, b, label_a, label_b): # pragma: no cover
    return '\n'.join(unified_diff(a.splitlines(), b.splitlines(), fromfile=label_a, tofile=label_b)) # pragma: no cover

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
