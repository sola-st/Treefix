from typing import Any # pragma: no cover
import difflib # pragma: no cover

src = 'original code sample' # pragma: no cover

from typing import Any # pragma: no cover
import difflib # pragma: no cover

def _format_str_once(dst: str, mode: Any) -> str: return dst + ' formatted' # pragma: no cover
dst = 'original code sample' # pragma: no cover
mode = 'standard' # pragma: no cover
def dump_to_file(mode: str, *args: str) -> str: return 'logfile.txt' # pragma: no cover
def diff(first: str, second: str, a_label: str, b_label: str) -> str: return '\n'.join(difflib.ndiff(first.splitlines(), second.splitlines())) # pragma: no cover
src = 'original code sample' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Raise AssertionError if `dst` reformats differently the second time."""
# We shouldn't call format_str() here, because that formats the string
# twice and may hide a bug where we bounce back and forth between two
# versions.
newdst = _format_str_once(dst, mode=mode)
_l_(5043)
if dst != newdst:
    _l_(5046)

    log = dump_to_file(
        str(mode),
        diff(src, dst, "source", "first pass"),
        diff(dst, newdst, "first pass", "second pass"),
    )
    _l_(5044)
    raise AssertionError(
        "INTERNAL ERROR: Black produced different code on the second pass of the"
        " formatter.  Please report a bug on https://github.com/psf/black/issues."
        f"  This diff might be helpful: {log}"
    ) from None
    _l_(5045)
