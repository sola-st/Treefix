from collections import namedtuple # pragma: no cover

Token = namedtuple('Token', ['type']) # pragma: no cover
token = type('MockToken', (), {'LPAR': Token('LPAR'), 'RPAR': Token('RPAR')})() # pragma: no cover
Node = namedtuple('Node', ['children']) # pragma: no cover
node = Node(children=[Token('LPAR'), 'wrapped_value', Token('RPAR')]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Returns `wrapped` if `node` is of the shape ( wrapped ).

    Parenthesis can be optional. Returns None otherwise"""
if len(node.children) != 3:
    _l_(5364)

    aux = None
    _l_(5363)
    exit(aux)

lpar, wrapped, rpar = node.children
_l_(5365)
if not (lpar.type == token.LPAR and rpar.type == token.RPAR):
    _l_(5367)

    aux = None
    _l_(5366)
    exit(aux)
aux = wrapped
_l_(5368)

exit(aux)
