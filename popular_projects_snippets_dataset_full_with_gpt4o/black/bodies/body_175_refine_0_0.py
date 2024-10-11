from typing import List, Tuple # pragma: no cover

line = type('Mock', (object,), {'depth': 1, 'enumerate_with_length': lambda self: [(0, type('Leaf', (object,), {'type': 'CLOSE', 'opening_bracket': 'first'})(), 1)], 'leaves': ['leaf1']})() # pragma: no cover
CLOSING_BRACKETS = ['CLOSE'] # pragma: no cover
first = 'first' # pragma: no cover
line_length = 100 # pragma: no cover
OPENING_BRACKETS = ['OPEN'] # pragma: no cover

line = type('Mock', (object,), {'depth': 1, 'enumerate_with_length': lambda self: iter([(0, type('Leaf', (object,), {'type': 'CLOSE', 'opening_bracket': 'first'})(), 1)]), 'leaves': [type('Leaf', (object,), {'type': 'CLOSE', 'opening_bracket': 'first'})()]})() # pragma: no cover
CLOSING_BRACKETS = ['CLOSE'] # pragma: no cover
first = 'first' # pragma: no cover
line_length = 100 # pragma: no cover
OPENING_BRACKETS = ['OPEN'] # pragma: no cover

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
