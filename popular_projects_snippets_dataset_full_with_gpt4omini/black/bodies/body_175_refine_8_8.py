from typing import List, Tuple # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self, leaves, depth):# pragma: no cover
        self.leaves = leaves# pragma: no cover
        self.depth = depth# pragma: no cover
    def enumerate_with_length(self):# pragma: no cover
        for leaf in self.leaves:# pragma: no cover
            yield leaf, len(leaf.value), len(leaf.value)# pragma: no cover
# pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, leaf_type, opening_bracket=None, value=''):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.opening_bracket = opening_bracket# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
OPENING_BRACKETS = ['(', '[', '{']# pragma: no cover
CLOSING_BRACKETS = [')', ']', '}']# pragma: no cover
first = '('  # pragma: no cover
line_length = 20  # pragma: no cover
line = MockLine(leaves=[MockLeaf('(', opening_bracket=first, value='a'), MockLeaf(')', opening_bracket=first, value='b')], depth=2) # pragma: no cover

from typing import List, Tuple # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, leaf_type, opening_bracket=None):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self, depth, leaves):# pragma: no cover
        self.depth = depth# pragma: no cover
        self.leaves = leaves# pragma: no cover
    def enumerate_with_length(self):# pragma: no cover
        for leaf in self.leaves:# pragma: no cover
            yield leaf, len(leaf.type), len(leaf.type) # pragma: no cover
line = MockLine(depth=2, leaves=[MockLeaf('(', None), MockLeaf(')', '('), MockLeaf('[', None), MockLeaf(']', None)]) # pragma: no cover
CLOSING_BRACKETS = [')', ']', '}'] # pragma: no cover
first = '(' # pragma: no cover
line_length = 20 # pragma: no cover
OPENING_BRACKETS = ['(', '[', '{'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""See `can_omit_invisible_parens`."""
remainder = False
_l_(5684)
length = 4 * line.depth
_l_(5685)
_index = -1
_l_(5686)
for _index, leaf, leaf_length in line.enumerate_with_length():
    _l_(5697)

    if leaf.type in CLOSING_BRACKETS and leaf.opening_bracket is first:
        _l_(5688)

        remainder = True
        _l_(5687)
    if remainder:
        _l_(5694)

        length += leaf_length
        _l_(5689)
        if length > line_length:
            _l_(5691)

            break
            _l_(5690)

        if leaf.type in OPENING_BRACKETS:
            _l_(5693)

            # There are brackets we can further split on.
            remainder = False
            _l_(5692)

else:
    # checked the entire string and line length wasn't exceeded
    if len(line.leaves) == _index + 1:
        _l_(5696)

        aux = True
        _l_(5695)
        exit(aux)
aux = False
_l_(5698)

exit(aux)
