import re # pragma: no cover
from typing import Pattern # pragma: no cover

regex = '^[a-z]+\n[a-z]+$' # pragma: no cover
Pattern = type('Pattern', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Compile a regular expression string in `regex`.

    If it contains newlines, use verbose mode.
    """
if "\n" in regex:
    _l_(17252)

    regex = "(?x)" + regex
    _l_(17251)
compiled: Pattern[str] = re.compile(regex)
_l_(17253)
aux = compiled
_l_(17254)
exit(aux)
