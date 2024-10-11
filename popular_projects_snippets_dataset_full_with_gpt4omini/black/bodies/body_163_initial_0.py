from dataclasses import dataclass # pragma: no cover

class Line:# pragma: no cover
    def __init__(self, mode, depth, inside_brackets, should_split_rhs, magic_trailing_comma):# pragma: no cover
        self.mode = mode# pragma: no cover
        self.depth = depth# pragma: no cover
        self.inside_brackets = inside_brackets# pragma: no cover
        self.should_split_rhs = should_split_rhs# pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma # pragma: no cover
self = type('Mock', (object,), {'mode': 'default', 'depth': 0, 'inside_brackets': False, 'should_split_rhs': True, 'magic_trailing_comma': True})() # pragma: no cover

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
_l_(6604)
exit(aux)
