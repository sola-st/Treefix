from typing import List, Tuple # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self, depth: int, leaves: List[Tuple[int, str, int]]):# pragma: no cover
        self.depth = depth# pragma: no cover
        self.leaves = leaves# pragma: no cover
    def enumerate_with_length(self):# pragma: no cover
        for item in self.leaves:# pragma: no cover
            yield item # pragma: no cover
line = MockLine(depth=1, leaves=[(0, '(', 1), (1, 'a', 1), (2, ')', 1)]) # pragma: no cover
class MockLast:# pragma: no cover
    def __init__(self, opening_bracket: str):# pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
last = MockLast(opening_bracket='(') # pragma: no cover
line_length = 10 # pragma: no cover
OPENING_BRACKETS = {'(', '[', '{'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""See `can_omit_invisible_parens`."""
length = 4 * line.depth
_l_(18734)
seen_other_brackets = False
_l_(18735)
for _index, leaf, leaf_length in line.enumerate_with_length():
    _l_(18742)

    length += leaf_length
    _l_(18736)
    if leaf is last.opening_bracket:
        _l_(18741)

        if seen_other_brackets or length <= line_length:
            _l_(18738)

            aux = True
            _l_(18737)
            exit(aux)

    elif leaf.type in OPENING_BRACKETS:
        _l_(18740)

        # There are brackets we can further split on.
        seen_other_brackets = True
        _l_(18739)
aux = False
_l_(18743)

exit(aux)
