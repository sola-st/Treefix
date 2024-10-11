from typing import Optional, Any # pragma: no cover

Line = type('Line', (object,), {}) # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'mode': 'default_mode',# pragma: no cover
    'depth': 0,# pragma: no cover
    'inside_brackets': False,# pragma: no cover
    'should_split_rhs': True,# pragma: no cover
    'magic_trailing_comma': False# pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
aux = Line(
    mode=self.mode,
    depth=self.depth,
    inside_brackets=self.inside_brackets,
    should_split_rhs=self.should_split_rhs,
    magic_trailing_comma=self.magic_trailing_comma,
)
_l_(18370)
exit(aux)
