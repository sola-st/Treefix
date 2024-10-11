import token # pragma: no cover
class MockNode: pass # pragma: no cover
class MockChild: pass # pragma: no cover

node = MockNode() # pragma: no cover
node.children = [MockChild(), MockChild(), MockChild()] # pragma: no cover
node.children[0].type = token.LPAR # pragma: no cover
node.children[1].type = 'wrapped_value' # pragma: no cover
node.children[2].type = token.RPAR # pragma: no cover

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
