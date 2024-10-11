from typing import List # pragma: no cover
class MockToken: pass # pragma: no cover
class MockSym: pass # pragma: no cover
class MockLeaf: pass # pragma: no cover

opening = MockLeaf() # pragma: no cover
opening.type = MockToken() # pragma: no cover
opening.bracket_depth = 0 # pragma: no cover
closing = MockLeaf() # pragma: no cover
closing.type = MockToken() # pragma: no cover
closing.bracket_depth = 1 # pragma: no cover
brackets = (opening.type, closing.type) # pragma: no cover
leaves = [opening, MockLeaf(), closing] # pragma: no cover
syms = type('MockSyms', (object,), {'arglist': MockToken(), 'typedargslist': MockToken()})() # pragma: no cover

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
