from collections import namedtuple # pragma: no cover

MockToken = namedtuple('MockToken', ['type']) # pragma: no cover
MockParent = namedtuple('MockParent', ['type']) # pragma: no cover
token = MockToken(type='COMMA') # pragma: no cover
syms = type('MockSyms', (object,), {'arglist': 'arglist', 'typedargslist': 'typedargslist'})() # pragma: no cover
opening = MockToken(type='opening') # pragma: no cover
closing = MockToken(type='closing') # pragma: no cover
brackets = (opening.type, closing.type) # pragma: no cover
leaf1 = MockToken(type='COMMA') # pragma: no cover
leaf2 = MockToken(type='other') # pragma: no cover
leaves = [opening, leaf1, leaf2, closing] # pragma: no cover

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
