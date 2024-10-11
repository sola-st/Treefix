import itertools # pragma: no cover

CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
first = '(' # pragma: no cover
line_length = 80 # pragma: no cover
OPENING_BRACKETS = {'(', '{', '['} # pragma: no cover
line = type('Mock', (object,), {'depth': 2, 'leaves': ['leaf1', 'leaf2', 'leaf3', 'leaf4'], 'enumerate_with_length': lambda self: itertools.zip_longest(range(len(self.leaves)), self.leaves, [10]*len(self.leaves))})() # pragma: no cover

import itertools # pragma: no cover

CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
first = '(' # pragma: no cover
line_length = 80 # pragma: no cover
OPENING_BRACKETS = {'(', '{', '['} # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, typ, bracket: setattr(self, 'type', typ) or setattr(self, 'opening_bracket', bracket)}) # pragma: no cover
line = type('Mock', (object,), {'depth': 2, 'leaves': [Leaf('type1', first), Leaf('type2', None), Leaf('CLOSE', first), Leaf('type4', None)], 'enumerate_with_length': lambda self: zip(range(len(self.leaves)), self.leaves, [10]*len(self.leaves))})() # pragma: no cover

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
