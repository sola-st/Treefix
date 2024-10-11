from typing import List, Optional # pragma: no cover
import token # pragma: no cover
import sys # pragma: no cover
from dataclasses import dataclass # pragma: no cover

class MockBracket: parent = None # pragma: no cover
opening_bracket = MockBracket() # pragma: no cover
opening_bracket.value = '[' # pragma: no cover
class MockLeaf: type = token.COMMA # pragma: no cover
class MockLine: leaves = [MockLeaf()] # pragma: no cover
mock_bracket_tracker = type('MockBracketTracker', (object,), {'max_delimiter_priority': lambda self, exclude: 2})() # pragma: no cover
magic_mode = type('MockMagicMode', (object,), {'magic_trailing_comma': True})() # pragma: no cover
line = MockLine() # pragma: no cover
line.bracket_tracker = mock_bracket_tracker # pragma: no cover
line.mode = magic_mode # pragma: no cover
COMMA_PRIORITY = 2 # pragma: no cover

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
