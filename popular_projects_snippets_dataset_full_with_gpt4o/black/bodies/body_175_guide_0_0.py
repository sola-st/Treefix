from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'opening_bracket']) # pragma: no cover
Line = namedtuple('Line', ['depth', 'enumerate_with_length', 'leaves']) # pragma: no cover
CLOSING_BRACKETS = {')', ']', '}'} # pragma: no cover
OPENING_BRACKETS = {'(', '[', '{'} # pragma: no cover
first = type('Mock', (object,), {}) # pragma: no cover
line_length = 50 # pragma: no cover
leaves = [Leaf(type='(', opening_bracket=first), Leaf(type=')', opening_bracket=first), Leaf(type='x', opening_bracket=None)] # pragma: no cover
def mock_enumerate_with_length(): # pragma: no cover
    for i, leaf in enumerate(leaves): # pragma: no cover
        yield i, leaf, len(leaf.type) # pragma: no cover
line = Line(depth=1, enumerate_with_length=mock_enumerate_with_length, leaves=leaves) # pragma: no cover

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
