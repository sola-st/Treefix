from typing import Any, Dict, Callable # pragma: no cover

_format_str_once = lambda dst, mode: dst.replace(' ', '_') # pragma: no cover
dst = 'def example_function(arg): return arg' # pragma: no cover
mode = 'black' # pragma: no cover
dump_to_file = lambda mode_str, src_diff, dst_diff: 'log.txt' # pragma: no cover
diff = lambda a, b, label_a, label_b: f'Diff between {label_a} and {label_b}' # pragma: no cover
src = 'def example_function(arg): return arg' # pragma: no cover

from typing import Callable, Any # pragma: no cover

_format_str_once = lambda dst, mode: dst.replace('old_version', 'new_version') # pragma: no cover
dst = 'def example_function(arg): return old_version' # pragma: no cover
mode = 'test_mode' # pragma: no cover
dump_to_file = lambda mode_str, src_diff, dst_diff: 'log.txt' # pragma: no cover
diff = lambda a, b, label_a, label_b: f'Diff between: {a} and {b}' # pragma: no cover
src = 'def example_function(arg): return old_version' # pragma: no cover

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
