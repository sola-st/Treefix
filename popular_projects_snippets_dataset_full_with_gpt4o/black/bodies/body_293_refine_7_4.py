import token # pragma: no cover
import types # pragma: no cover

opening = type('Mock', (object,), {'type': 'LPAREN'})() # pragma: no cover
closing = type('Mock', (object,), {'type': 'RPAREN', 'bracket_depth': 1})() # pragma: no cover
brackets = ('LPAREN', 'RPAREN') # pragma: no cover
leaves = [opening, type('Mock', (object,), {'type': token.COMMA, 'bracket_depth': 1, 'parent': None})(), closing] # pragma: no cover
token = type('Mock', (object,), {'COMMA': 'COMMA'}) # pragma: no cover
syms = type('Mock', (object,), {'arglist': 'arglist', 'typedargslist': 'typedargslist'}) # pragma: no cover

import enum # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class TokenType(enum.Enum):# pragma: no cover
    COMMA = 'comma' # pragma: no cover
class SymbolType(enum.Enum):# pragma: no cover
    ARGLIST = 'arglist'# pragma: no cover
    TYPEDARGSLIST = 'typedargslist' # pragma: no cover
token = SimpleNamespace(COMMA=TokenType.COMMA) # pragma: no cover
syms = SimpleNamespace(arglist=SymbolType.ARGLIST, typedargslist=SymbolType.TYPEDARGSLIST) # pragma: no cover
brackets = ('open_paren', 'close_paren') # pragma: no cover
Leaf = SimpleNamespace # pragma: no cover
opening = Leaf(type='open_paren', bracket_depth=0, parent=None) # pragma: no cover
closing = Leaf(type='close_paren', bracket_depth=1, parent=None) # pragma: no cover
leaves = [opening, Leaf(type='name', bracket_depth=0, parent=None), Leaf(type=token.COMMA, bracket_depth=1, parent=SimpleNamespace(type=syms.arglist)), closing] # pragma: no cover

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
