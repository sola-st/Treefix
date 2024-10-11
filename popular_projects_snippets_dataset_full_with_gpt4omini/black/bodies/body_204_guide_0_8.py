from typing import Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

dst = 'print(  '  # Some initial string that simulates code before formatting. # pragma: no cover
src = 'print(    )'  # Original source code string that is different from dst. # pragma: no cover
mode = 'fast'  # Example mode string. # pragma: no cover
def diff(a: str, b: str, label_a: str, label_b: str) -> str: return f'Difference between {label_a} and {label_b}: {a} -> {b}'  # Mocking diff function. # pragma: no cover
_format_str_once = lambda x, mode: x.replace('    ', '  ')  # Mocking _format_str_once function. # pragma: no cover

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
