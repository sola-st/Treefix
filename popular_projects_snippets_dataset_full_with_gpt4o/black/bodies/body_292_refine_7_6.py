from typing import Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover

node = SimpleNamespace(type='atom', children=[]) # pragma: no cover
syms = type('Syms', (object,), {'atom': 'atom', 'testlist_gexp': 'testlist_gexp', 'namedexpr_test': 'namedexpr_test'}) # pragma: no cover
def unwrap_singleton_parenthesis(n: Any) -> Any:# pragma: no cover
    if n.type == 'atom':# pragma: no cover
        return SimpleNamespace(type='testlist_gexp', children=[SimpleNamespace(type='namedexpr_test')])# pragma: no cover
    return None # pragma: no cover

from typing import List, Optional # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type, children=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children if children else [] # pragma: no cover
def unwrap_singleton_parenthesis(node: Node) -> Optional[Node]:# pragma: no cover
    return node.children[0] if len(node.children) == 1 else None # pragma: no cover
syms = type('Syms', (object,), {# pragma: no cover
    'atom': 1,# pragma: no cover
    'testlist_gexp': 2,# pragma: no cover
    'namedexpr_test': 3# pragma: no cover
}) # pragma: no cover
node = Node(syms.atom, [Node(syms.testlist_gexp, [Node(syms.namedexpr_test)])]) # pragma: no cover

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
