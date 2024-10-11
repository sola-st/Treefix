import token # pragma: no cover
from typing import Optional, Set, Any # pragma: no cover

class MockNode:  # For `opening_bracket` # pragma: no cover
    def __init__(self, parent=None, value=None): # pragma: no cover
        self.parent = parent # pragma: no cover
        self.value = value # pragma: no cover
        self.type = None # pragma: no cover
class MockLine:  # For `line` # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.bracket_tracker = MockBracketTracker() # pragma: no cover
        self.mode = MockMode() # pragma: no cover
class MockBracketTracker: # pragma: no cover
    def max_delimiter_priority(self, exclude: Set[int]) -> int: # pragma: no cover
        return 1  # Simulating a priority value # pragma: no cover
class MockMode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magic_trailing_comma = True # pragma: no cover
opening_bracket = MockNode(parent=None, value='(')  # Example of an opening bracket # pragma: no cover
line = MockLine() # pragma: no cover

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
