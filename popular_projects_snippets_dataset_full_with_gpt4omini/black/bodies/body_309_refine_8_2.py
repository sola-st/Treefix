from unittest.mock import Mock # pragma: no cover
import token # pragma: no cover

node = Mock() # pragma: no cover
node.children = [Mock(type=token.LPAR), Mock(), Mock(type=token.RPAR)] # pragma: no cover

from collections import namedtuple # pragma: no cover

Token = namedtuple('Token', ['type']) # pragma: no cover
class MockNode: children = [Token(type='LPAR'), 'wrapped_value', Token(type='RPAR')] # pragma: no cover
node = MockNode() # pragma: no cover
class MockToken: LPAR = 'LPAR'; RPAR = 'RPAR' # pragma: no cover
token = MockToken() # pragma: no cover

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
