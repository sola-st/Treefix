import token # pragma: no cover

brackets = ('OP', 'CL') # pragma: no cover
MockLeaf = type('MockLeaf', (object,), {'bracket_depth': 0, 'type': None, 'parent': None}) # pragma: no cover
opening = MockLeaf() # pragma: no cover
opening.type = 'OP' # pragma: no cover
closing = MockLeaf() # pragma: no cover
closing.type = 'CL' # pragma: no cover
closing.bracket_depth = 0 # pragma: no cover
leaves = [MockLeaf(), opening, MockLeaf(), closing] # pragma: no cover
leaves[2].type = token.COMMA # pragma: no cover
leaves[2].bracket_depth = 1 # pragma: no cover
leaves[2].parent = type('Parent', (object,), {'type': 'arglist'})() # pragma: no cover
syms = type('syms', (object,), {'arglist': 'arglist', 'typedargslist': 'typedargslist'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if content between `opening` and `closing` is a one-sequence."""
if (opening.type, closing.type) != brackets:
    _l_(19118)

    aux = False
    _l_(19117)
    exit(aux)

depth = closing.bracket_depth + 1
_l_(19119)
for _opening_index, leaf in enumerate(leaves):
    _l_(19123)

    if leaf is opening:
        _l_(19121)

        break
        _l_(19120)

else:
    raise LookupError("Opening paren not found in `leaves`")
    _l_(19122)

commas = 0
_l_(19124)
_opening_index += 1
_l_(19125)
for leaf in leaves[_opening_index:]:
    _l_(19134)

    if leaf is closing:
        _l_(19127)

        break
        _l_(19126)

    bracket_depth = leaf.bracket_depth
    _l_(19128)
    if bracket_depth == depth and leaf.type == token.COMMA:
        _l_(19133)

        commas += 1
        _l_(19129)
        if leaf.parent and leaf.parent.type in {
            syms.arglist,
            syms.typedargslist,
        }:
            _l_(19132)

            commas += 1
            _l_(19130)
            break
            _l_(19131)
aux = commas < 2
_l_(19135)

exit(aux)
