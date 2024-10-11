import token # pragma: no cover

node = type('MockNode', (object,), {'children': [type('MockToken', (object,), {'type': token.LPAR})(), 'wrapped', type('MockToken', (object,), {'type': token.RPAR})()]})() # pragma: no cover
token.LPAR = 7 # pragma: no cover
token.RPAR = 8 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Returns `wrapped` if `node` is of the shape ( wrapped ).

    Parenthesis can be optional. Returns None otherwise"""
if len(node.children) != 3:
    _l_(16867)

    aux = None
    _l_(16866)
    exit(aux)

lpar, wrapped, rpar = node.children
_l_(16868)
if not (lpar.type == token.LPAR and rpar.type == token.RPAR):
    _l_(16870)

    aux = None
    _l_(16869)
    exit(aux)
aux = wrapped
_l_(16871)

exit(aux)
