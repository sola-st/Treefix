from typing import Any # pragma: no cover

class Line:# pragma: no cover
    def __init__(self, mode: Any, depth: int, inside_brackets: bool, should_split_rhs: bool, magic_trailing_comma: bool):# pragma: no cover
        self.mode = mode# pragma: no cover
        self.depth = depth# pragma: no cover
        self.inside_brackets = inside_brackets# pragma: no cover
        self.should_split_rhs = should_split_rhs# pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'mode': 'example_mode',# pragma: no cover
    'depth': 3,# pragma: no cover
    'inside_brackets': True,# pragma: no cover
    'should_split_rhs': False,# pragma: no cover
    'magic_trailing_comma': True# pragma: no cover
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
