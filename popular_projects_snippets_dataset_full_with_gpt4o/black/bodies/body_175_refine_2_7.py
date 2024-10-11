from typing import List, Tuple # pragma: no cover
from types import SimpleNamespace # pragma: no cover

line = SimpleNamespace( # pragma: no cover
    depth=1, # pragma: no cover
    enumerate_with_length=lambda: iter([ # pragma: no cover
        (0, SimpleNamespace(type='closed', opening_bracket=False), 10), # pragma: no cover
        (1, SimpleNamespace(type='open', opening_bracket=True), 5), # pragma: no cover
    ]), # pragma: no cover
    leaves=[SimpleNamespace(type='closed', opening_bracket=False), SimpleNamespace(type='open', opening_bracket=True)] # pragma: no cover
) # pragma: no cover
CLOSING_BRACKETS = {'closed'} # pragma: no cover
first = False # pragma: no cover
line_length = 50 # pragma: no cover
OPENING_BRACKETS = {'open'} # pragma: no cover

from itertools import zip_longest # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type, opening_bracket): # pragma: no cover
        self.type = type # pragma: no cover
        self.opening_bracket = opening_bracket # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.depth = 4 # pragma: no cover
        self.leaves = [ # pragma: no cover
            Leaf(type='OPEN', opening_bracket='first'), # pragma: no cover
            Leaf(type='CLOSE', opening_bracket='first'), # pragma: no cover
            Leaf(type='TEXT', opening_bracket=None), # pragma: no cover
        ] # pragma: no cover
    def enumerate_with_length(self): # pragma: no cover
        return zip_longest(range(len(self.leaves)), self.leaves, [10, 20, 30]) # pragma: no cover
 # pragma: no cover
line = Line() # pragma: no cover
CLOSING_BRACKETS = {'CLOSE'} # pragma: no cover
first = 'first' # pragma: no cover
line_length = 50 # pragma: no cover
OPENING_BRACKETS = {'OPEN'} # pragma: no cover

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
