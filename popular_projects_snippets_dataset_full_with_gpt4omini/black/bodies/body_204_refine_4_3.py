from typing import Callable, Any # pragma: no cover
import difflib # pragma: no cover

_format_str_once = lambda s, mode: s.replace(' ', '') # pragma: no cover
dst = 'def example_function():\n    print("Hello")' # pragma: no cover
mode = 'default' # pragma: no cover
dump_to_file = lambda mode, *args: f'Dump: {mode}, {args}' # pragma: no cover
diff = lambda a, b, label_a, label_b: difflib.ndiff(a.splitlines(), b.splitlines()) # pragma: no cover
src = 'def example_function():\n    print("Hello World")' # pragma: no cover

from typing import Callable, Any # pragma: no cover
import difflib # pragma: no cover

_format_str_once = lambda s, mode: s.replace('World', 'Universe') # pragma: no cover
dst = 'def example_function():\n    print("Hello Universe")' # pragma: no cover
mode = 'default' # pragma: no cover
dump_to_file = lambda mode, src_diff, dst_diff: 'log.txt' # pragma: no cover
diff = lambda a, b, label_a, label_b: '\n'.join(list(difflib.ndiff(a.splitlines(), b.splitlines()))) # pragma: no cover
src = 'def example_function():\n    print("Hello World")' # pragma: no cover

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
