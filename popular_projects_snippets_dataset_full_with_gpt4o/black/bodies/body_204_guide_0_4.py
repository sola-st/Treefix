import difflib # pragma: no cover
import tempfile # pragma: no cover

def _format_str_once(s: str, mode: str) -> str: # pragma: no cover
    return s + '_formatted' # pragma: no cover
 # pragma: no cover
def diff(a: str, b: str, desc_a: str, desc_b: str) -> str: # pragma: no cover
    return '\n'.join(difflib.unified_diff(a.splitlines(), b.splitlines(), # pragma: no cover
                         fromfile=desc_a, tofile=desc_b, lineterm='')) # pragma: no cover
 # pragma: no cover
def dump_to_file(mode, *diffs) -> str: # pragma: no cover
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.diff') as f: # pragma: no cover
        for diff in diffs: # pragma: no cover
            f.write(diff) # pragma: no cover
            f.write('\n') # pragma: no cover
        return f.name # pragma: no cover
 # pragma: no cover
src = 'some code' # pragma: no cover
dst = 'some code' # pragma: no cover
mode = 'some_mode' # pragma: no cover
 # pragma: no cover
# Modify dst to trigger the uncovered code path # pragma: no cover
dst = 'some code_modified' # pragma: no cover
newdst = _format_str_once(dst, mode=mode) # pragma: no cover

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
