from collections import namedtuple # pragma: no cover
import token # pragma: no cover
import sys # pragma: no cover

Bracket = namedtuple('Bracket', ['parent', 'value']) # pragma: no cover
opening_bracket = Bracket(parent=type('Mock', (object,), {'type': 'mock_type'}), value='[') # pragma: no cover
Line = namedtuple('Line', ['leaves', 'bracket_tracker', 'mode']) # pragma: no cover
line = Line(leaves=[type('Mock', (object,), {'type': token.COMMA})], bracket_tracker=type('Mock', (object,), {'max_delimiter_priority': lambda self, exclude: 1})(), mode=type('Mock', (object,), {'magic_trailing_comma': True})()) # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover

import token # pragma: no cover
from typing import List, Set # pragma: no cover

class MockNode:  # Mock for nodes in the line structure # pragma: no cover
    def __init__(self, type, value=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.parent = None # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class MockBracketTracker:  # Mock for bracket tracker # pragma: no cover
    def max_delimiter_priority(self, exclude: Set[int]) -> int: # pragma: no cover
        return COMMA_PRIORITY # pragma: no cover
 # pragma: no cover
class MockMode:  # Mock for mode attributes # pragma: no cover
    def __init__(self, magic_trailing_comma): # pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma # pragma: no cover
 # pragma: no cover
class MockLine:  # Mock for line object # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.bracket_tracker = MockBracketTracker() # pragma: no cover
        self.mode = MockMode(True) # pragma: no cover
 # pragma: no cover
class MockSyms:  # Mock for syms # pragma: no cover
    atom = 'atom' # pragma: no cover
 # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
opening_bracket = MockNode(type='opening_bracket', value='[') # pragma: no cover
line = MockLine() # pragma: no cover
leaf1 = MockNode(type=token.COMMA) # pragma: no cover
leaf2 = MockNode(type='other') # pragma: no cover
line.leaves = [leaf1, leaf2] # pragma: no cover
opening_bracket.parent = MockNode(type='parent', value='parent_value') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Should `line` be immediately split with `delimiter_split()` after RHS?"""

if not (opening_bracket.parent and opening_bracket.value in "[{("):
    _l_(5109)

    aux = False
    _l_(5108)
    exit(aux)

# We're essentially checking if the body is delimited by commas and there's more
# than one of them (we're excluding the trailing comma and if the delimiter priority
# is still commas, that means there's more).
exclude = set()
_l_(5110)
trailing_comma = False
_l_(5111)
try:
    _l_(5119)

    last_leaf = line.leaves[-1]
    _l_(5112)
    if last_leaf.type == token.COMMA:
        _l_(5115)

        trailing_comma = True
        _l_(5113)
        exclude.add(id(last_leaf))
        _l_(5114)
    max_priority = line.bracket_tracker.max_delimiter_priority(exclude=exclude)
    _l_(5116)
except (IndexError, ValueError):
    _l_(5118)

    aux = False
    _l_(5117)
    exit(aux)
aux = max_priority == COMMA_PRIORITY and (
    (line.mode.magic_trailing_comma and trailing_comma)
    # always explode imports
    or opening_bracket.parent.type in {syms.atom, syms.import_from}
)
_l_(5120)

exit(aux)
