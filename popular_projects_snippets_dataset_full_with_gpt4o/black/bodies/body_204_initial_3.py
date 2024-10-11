from typing import Any, Callable # pragma: no cover
import random # pragma: no cover

_format_str_once: Callable[[str, Any], str] = lambda dst, mode: dst[::-1] # pragma: no cover
dst: str = 'initial code' # pragma: no cover
mode: Any = {'mode_name': 'dummy_mode'} # pragma: no cover
dump_to_file: Callable[..., str] = lambda *args, **kwargs: 'logfile.txt' # pragma: no cover
diff: Callable[[str, str, str, str], str] = lambda x, y, a, b: f'Diff between {a} and {b}: {x} -> {y}' # pragma: no cover
src: str = 'source code' # pragma: no cover

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
