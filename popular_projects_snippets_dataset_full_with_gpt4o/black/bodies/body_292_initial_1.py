from typing import Optional # pragma: no cover

node = type('Node', (object,), {'type': 'atom'})() # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 'atom', 'testlist_gexp': 'testlist_gexp', 'namedexpr_test': 'namedexpr_test'})() # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    if node.type == 'atom':# pragma: no cover
        return type('GexpNode', (object,), {'type': 'testlist_gexp', 'children': [type('ChildNode', (object,), {'type': 'namedexpr_test'})()]})()# pragma: no cover
    return None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` holds a tuple that contains a walrus operator."""
if node.type != syms.atom:
    _l_(17730)

    aux = False
    _l_(17729)
    exit(aux)
gexp = unwrap_singleton_parenthesis(node)
_l_(17731)
if gexp is None or gexp.type != syms.testlist_gexp:
    _l_(17733)

    aux = False
    _l_(17732)
    exit(aux)
aux = any(child.type == syms.namedexpr_test for child in gexp.children)
_l_(17734)

exit(aux)
