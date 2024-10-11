from typing import List, Any # pragma: no cover
import sys # pragma: no cover

node = type('MockNode', (object,), {'children': [type('MockToken', (object,), {'type': 'LPAR'})(), 'wrapped_value', type('MockToken', (object,), {'type': 'RPAR'})()]})() # pragma: no cover
token = type('MockTokenModule', (object,), {'LPAR': 'LPAR', 'RPAR': 'RPAR'})() # pragma: no cover

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
