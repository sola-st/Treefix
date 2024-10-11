from typing import List, Tuple # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self, depth: int, leaves: List[Tuple[str, int]]) -> None:# pragma: no cover
        self.depth = depth# pragma: no cover
        self.leaves = leaves# pragma: no cover
# pragma: no cover
    def enumerate_with_length(self) -> List[Tuple[int, str, int]]:# pragma: no cover
        return [(i, leaf[0], leaf[1]) for i, leaf in enumerate(self.leaves)] # pragma: no cover
line = MockLine(depth=3, leaves=[('a', 1), ('b', 1), ('(', 1), (')', 1)]) # pragma: no cover
class MockLast:# pragma: no cover
    opening_bracket = '(' # pragma: no cover
last = MockLast() # pragma: no cover
line_length = 10 # pragma: no cover
OPENING_BRACKETS = {'(', '[', '{', '<'} # pragma: no cover

from typing import List, Dict # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type_str):# pragma: no cover
        self.type = type_str# pragma: no cover
# pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self, depth: int, leaves: List[MockLeaf]) -> None:# pragma: no cover
        self.depth = depth# pragma: no cover
        self.leaves = leaves# pragma: no cover
# pragma: no cover
    def enumerate_with_length(self):# pragma: no cover
        for leaf in self.leaves:# pragma: no cover
            yield leaf, 1  # assuming length is 1 for each leaf # pragma: no cover
line = MockLine(2, [MockLeaf('('), MockLeaf(')'), MockLeaf('['), MockLeaf(']')]) # pragma: no cover
class MockLast:# pragma: no cover
    opening_bracket = MockLeaf('(') # pragma: no cover
last = MockLast() # pragma: no cover
line_length = 10 # pragma: no cover
OPENING_BRACKETS = {'(', '[', '{'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""See `can_omit_invisible_parens`."""
length = 4 * line.depth
_l_(6975)
seen_other_brackets = False
_l_(6976)
for _index, leaf, leaf_length in line.enumerate_with_length():
    _l_(6983)

    length += leaf_length
    _l_(6977)
    if leaf is last.opening_bracket:
        _l_(6982)

        if seen_other_brackets or length <= line_length:
            _l_(6979)

            aux = True
            _l_(6978)
            exit(aux)

    elif leaf.type in OPENING_BRACKETS:
        _l_(6981)

        # There are brackets we can further split on.
        seen_other_brackets = True
        _l_(6980)
aux = False
_l_(6984)

exit(aux)
