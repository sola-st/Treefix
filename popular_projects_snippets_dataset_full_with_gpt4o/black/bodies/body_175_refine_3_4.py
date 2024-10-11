from typing import List, Tuple, Any # pragma: no cover

line = type("Mock", (object,), {"depth": 2, "enumerate_with_length": lambda self: [(0, type("Leaf", (object,), {"type": ")", "opening_bracket": "(", "length": 2})(), 2), (1, type("Leaf", (object,), {"type": "(", "opening_bracket": "(", "length": 4})(), 4)], "leaves": [None, None]})() # pragma: no cover
CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
first = "(" # pragma: no cover
line_length = 50 # pragma: no cover
OPENING_BRACKETS = {'(', '{', '['} # pragma: no cover

from typing import List, Tuple, Any # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type, opening_bracket): # pragma: no cover
        self.type = type # pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.depth = 2 # pragma: no cover
        self.leaves = [Leaf(')', '('), Leaf('(', '('), Leaf(')', ')'), Leaf('(', ')')] # pragma: no cover
 # pragma: no cover
    def enumerate_with_length(self): # pragma: no cover
        return [(i, leaf, 10) for i, leaf in enumerate(self.leaves)] # pragma: no cover
 # pragma: no cover
line = Line() # pragma: no cover
CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
first = '(' # pragma: no cover
line_length = 50 # pragma: no cover
OPENING_BRACKETS = {'(', '{', '['} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""See `can_omit_invisible_parens`."""
remainder = False
_l_(17118)
length = 4 * line.depth
_l_(17119)
_index = -1
_l_(17120)
for _index, leaf, leaf_length in line.enumerate_with_length():
    _l_(17131)

    if leaf.type in CLOSING_BRACKETS and leaf.opening_bracket is first:
        _l_(17122)

        remainder = True
        _l_(17121)
    if remainder:
        _l_(17128)

        length += leaf_length
        _l_(17123)
        if length > line_length:
            _l_(17125)

            break
            _l_(17124)

        if leaf.type in OPENING_BRACKETS:
            _l_(17127)

            # There are brackets we can further split on.
            remainder = False
            _l_(17126)

else:
    # checked the entire string and line length wasn't exceeded
    if len(line.leaves) == _index + 1:
        _l_(17130)

        aux = True
        _l_(17129)
        exit(aux)
aux = False
_l_(17132)

exit(aux)
