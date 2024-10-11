import re # pragma: no cover
from typing import Pattern # pragma: no cover

regex = r'some pattern\n with newlines' # pragma: no cover
Pattern = type('Mock', (object,), {'__init__': lambda self: None}) # pragma: no cover
re = type('Mock', (object,), {'compile': lambda self, x: 'compiled_' + x}) # pragma: no cover

import re # pragma: no cover
from typing import Pattern # pragma: no cover

regex = '^(\w+)\\n(\w+)$' # pragma: no cover
class MockPattern: pass # pragma: no cover
class MockRe: # pragma: no cover
    @staticmethod# pragma: no cover
    def compile(pattern): return 'compiled_' + pattern # pragma: no cover
Pattern = MockPattern # pragma: no cover
re = MockRe # pragma: no cover

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
