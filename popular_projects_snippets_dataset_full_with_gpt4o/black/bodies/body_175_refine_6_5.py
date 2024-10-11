from typing import List, Tuple # pragma: no cover

class MockLeaf: # pragma: no cover
    def __init__(self, type, opening_bracket=None): # pragma: no cover
        self.type = type; # pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, depth, leaves: List[Tuple[int, MockLeaf, int]]): # pragma: no cover
        self.depth = depth # pragma: no cover
        self._leaves = leaves # pragma: no cover
    def enumerate_with_length(self): # pragma: no cover
        for idx, (type, leaf, l_length) in enumerate(self._leaves): # pragma: no cover
            yield idx, leaf, l_length # pragma: no cover
    @property # pragma: no cover
    def leaves(self): # pragma: no cover
        return [leaf for _, leaf, _ in self._leaves] # pragma: no cover
 # pragma: no cover
line = MockLine(1, [ # pragma: no cover
    (1, MockLeaf('type1', 'first'), 5), # pragma: no cover
    (2, MockLeaf(')')) # pragma: no cover
]) # pragma: no cover
 # pragma: no cover
CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
first = 'first' # pragma: no cover
line_length = 10 # pragma: no cover
OPENING_BRACKETS = {'(', '{', '['} # pragma: no cover

from typing import List, Tuple # pragma: no cover

class MockLeaf: # pragma: no cover
    def __init__(self, type, opening_bracket=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, depth, leaves: List[Tuple[int, MockLeaf, int]]): # pragma: no cover
        self.depth = depth # pragma: no cover
        self._leaves = leaves # pragma: no cover
    def enumerate_with_length(self): # pragma: no cover
        for idx, leaf in enumerate(self._leaves): # pragma: no cover
            yield idx, leaf[1], leaf[2] # pragma: no cover
    @property # pragma: no cover
    def leaves(self): # pragma: no cover
        return [leaf[1] for leaf in self._leaves] # pragma: no cover
 # pragma: no cover
line = MockLine(1, [ # pragma: no cover
    (0, MockLeaf(')', 'first'), 5), # pragma: no cover
    (1, MockLeaf('(', None), 10) # pragma: no cover
]) # pragma: no cover
 # pragma: no cover
CLOSING_BRACKETS = {')', '}', ']'} # pragma: no cover
first = 'first' # pragma: no cover
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
