from typing import List, Optional # pragma: no cover

class MockToken: COMMA = 'COMMA' # pragma: no cover
class MockSyms: arglist = 'arglist'; typedargslist = 'typedargslist' # pragma: no cover

from typing import List, Optional # pragma: no cover

class MockToken:# pragma: no cover
    COMMA = 'comma' # pragma: no cover
class MockSyms:# pragma: no cover
    arglist = 'arglist'# pragma: no cover
    typedargslist = 'typedargslist' # pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, type, bracket_depth, parent=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.bracket_depth = bracket_depth# pragma: no cover
        self.parent = parent # pragma: no cover
opening = MockLeaf(type='(', bracket_depth=1, parent=None) # pragma: no cover
closing = MockLeaf(type=')', bracket_depth=1, parent=None) # pragma: no cover
brackets = (opening.type, closing.type) # pragma: no cover
leaves = [opening, MockLeaf(type=MockToken.COMMA, bracket_depth=1), closing] # pragma: no cover
token = MockToken() # pragma: no cover
syms = MockSyms() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if content between `opening` and `closing` is a one-sequence."""
if (opening.type, closing.type) != brackets:
    _l_(7134)

    aux = False
    _l_(7133)
    exit(aux)

depth = closing.bracket_depth + 1
_l_(7135)
for _opening_index, leaf in enumerate(leaves):
    _l_(7139)

    if leaf is opening:
        _l_(7137)

        break
        _l_(7136)

else:
    raise LookupError("Opening paren not found in `leaves`")
    _l_(7138)

commas = 0
_l_(7140)
_opening_index += 1
_l_(7141)
for leaf in leaves[_opening_index:]:
    _l_(7150)

    if leaf is closing:
        _l_(7143)

        break
        _l_(7142)

    bracket_depth = leaf.bracket_depth
    _l_(7144)
    if bracket_depth == depth and leaf.type == token.COMMA:
        _l_(7149)

        commas += 1
        _l_(7145)
        if leaf.parent and leaf.parent.type in {
            syms.arglist,
            syms.typedargslist,
        }:
            _l_(7148)

            commas += 1
            _l_(7146)
            break
            _l_(7147)
aux = commas < 2
_l_(7151)

exit(aux)
