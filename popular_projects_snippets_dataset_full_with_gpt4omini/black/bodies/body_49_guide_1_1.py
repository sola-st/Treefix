import token # pragma: no cover
from typing import Set # pragma: no cover

class MockLeaf:  # Mock class for a leaf # pragma: no cover
    def __init__(self, leaf_type): # pragma: no cover
        self.type = leaf_type # pragma: no cover
 # pragma: no cover
class MockBracketTracker:  # Mock class for bracket tracker # pragma: no cover
    def max_delimiter_priority(self, exclude: Set[int]): # pragma: no cover
        return COMMA_PRIORITY # pragma: no cover
 # pragma: no cover
class MockMode:  # Mock class for mode containing magic_trailing_comma # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magic_trailing_comma = True # pragma: no cover
 # pragma: no cover
class MockLine:  # Mock class for line # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [MockLeaf(token.COMMA)] # pragma: no cover
# Last leaf is of type COMMA # pragma: no cover
        self.bracket_tracker = MockBracketTracker() # pragma: no cover
        self.mode = MockMode() # pragma: no cover
 # pragma: no cover
class MockOpeningBracket:  # Mock class for opening bracket # pragma: no cover
    def __init__(self): # pragma: no cover
        self.parent = MockParent() # pragma: no cover
        self.value = '[' # pragma: no cover
 # pragma: no cover
class MockParent:  # Mock parent class # pragma: no cover
    @property # pragma: no cover
    def type(self): # pragma: no cover
        return syms.atom # pragma: no cover
# This will hit the condition in the code # pragma: no cover
 # pragma: no cover
line = MockLine() # pragma: no cover
opening_bracket = MockOpeningBracket() # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover

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
