from typing import List, Tuple # pragma: no cover

class MockLeaf: # pragma: no cover
    def __init__(self, leaf_type, opening_bracket=None): # pragma: no cover
        self.type = leaf_type # pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
    def enumerate_with_length(self) -> Tuple[int, 'MockLeaf', int]: # pragma: no cover
        for index, leaf in enumerate(self.leaves): # pragma: no cover
            yield index, leaf, 1 # pragma: no cover
  # Assuming each leaf has a length of 1 # pragma: no cover
 # pragma: no cover
OPENING_BRACKETS = {'('} # pragma: no cover
CLOSING_BRACKETS = {')'} # pragma: no cover
 # pragma: no cover
# Initialize the objects to hit uncovered paths # pragma: no cover
first = '(' # pragma: no cover
leaf1 = MockLeaf('(') # pragma: no cover
leaf2 = MockLeaf(')') # pragma: no cover
line = MockLine([leaf1, leaf2]) # pragma: no cover
line_length = 5 # pragma: no cover
line.depth = 2 # pragma: no cover
aux = False # pragma: no cover
remainder = False # pragma: no cover

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
