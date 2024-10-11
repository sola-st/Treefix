import token # pragma: no cover
from typed_ast import ast3 as ast # pragma: no cover
from typing import Set, Any # pragma: no cover

COMMA_PRIORITY = 1 # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, value=None, parent=None, type=None): # pragma: no cover
        self.value = value # pragma: no cover
        self.parent = parent # pragma: no cover
        self.type = type # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = MockBracketTracker() # pragma: no cover
        self.leaves = [ # pragma: no cover
            MockNode(value=',', type=token.COMMA), # pragma: no cover
            MockNode(value='}', type=token.RBRACE) # pragma: no cover
        ] # pragma: no cover
        self.mode = MockMode(magic_trailing_comma=True) # pragma: no cover
class MockBracketTracker: # pragma: no cover
    def max_delimiter_priority(self, exclude: Set[Any] = set()): # pragma: no cover
        return COMMA_PRIORITY # pragma: no cover
class MockMode: # pragma: no cover
    def __init__(self, magic_trailing_comma): # pragma: no cover
        self.magic_trailing_comma = magic_trailing_comma # pragma: no cover
opening_bracket = MockNode(value='[', parent=None) # pragma: no cover
line = MockLine() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Should `line` be immediately split with `delimiter_split()` after RHS?"""

if not (opening_bracket.parent and opening_bracket.value in "[{("):
    _l_(16889)

    aux = False
    _l_(16888)
    exit(aux)

# We're essentially checking if the body is delimited by commas and there's more
# than one of them (we're excluding the trailing comma and if the delimiter priority
# is still commas, that means there's more).
exclude = set()
_l_(16890)
trailing_comma = False
_l_(16891)
try:
    _l_(16899)

    last_leaf = line.leaves[-1]
    _l_(16892)
    if last_leaf.type == token.COMMA:
        _l_(16895)

        trailing_comma = True
        _l_(16893)
        exclude.add(id(last_leaf))
        _l_(16894)
    max_priority = line.bracket_tracker.max_delimiter_priority(exclude=exclude)
    _l_(16896)
except (IndexError, ValueError):
    _l_(16898)

    aux = False
    _l_(16897)
    exit(aux)
aux = max_priority == COMMA_PRIORITY and (
    (line.mode.magic_trailing_comma and trailing_comma)
    # always explode imports
    or opening_bracket.parent.type in {syms.atom, syms.import_from}
)
_l_(16900)

exit(aux)
