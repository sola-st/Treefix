import re # pragma: no cover
from re import Pattern # pragma: no cover

regex = 'sample-regex' # pragma: no cover
Pattern = re.Pattern if hasattr(re, 'Pattern') else type('Pattern', (object,), {}) # pragma: no cover
re.compile = re.compile if hasattr(re, 'compile') else lambda x: type('CompiledPattern', (object,), {}) # pragma: no cover

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
