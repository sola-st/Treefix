import re # pragma: no cover
from typing import Pattern # pragma: no cover

regex = 'your\nregex\npattern' # pragma: no cover
Pattern = type('MockPattern', (object,), {'__init__': lambda self: None}) # pragma: no cover
re = type('MockRe', (object,), {'compile': lambda pattern: 'compiled_pattern'}) # pragma: no cover

import re # pragma: no cover
from typing import Pattern # pragma: no cover

regex = r'^[a-zA-Z0-9]+$' # pragma: no cover
Pattern = type('MockPattern', (object,), {}) # pragma: no cover
re = type('MockRe', (object,), {'compile': lambda self, pattern: 'compiled_pattern'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Compile a regular expression string in `regex`.

    If it contains newlines, use verbose mode.
    """
if "\n" in regex:
    _l_(5824)

    regex = "(?x)" + regex
    _l_(5823)
compiled: Pattern[str] = re.compile(regex)
_l_(5825)
aux = compiled
_l_(5826)
exit(aux)
