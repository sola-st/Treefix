from typing import NamedTuple # pragma: no cover
import collections # pragma: no cover

syms = type('Mock', (object,), {# pragma: no cover
    'atom': 0, # pragma: no cover
    'testlist_gexp': 1, # pragma: no cover
    'namedexpr_test': 2# pragma: no cover
}) # pragma: no cover
class Node(NamedTuple):# pragma: no cover
    type: int# pragma: no cover
    children: list # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    if len(node.children) == 1 and isinstance(node.children[0], Node):# pragma: no cover
        return node.children[0]# pragma: no cover
    return None # pragma: no cover
node = Node(type=0, children=[Node(type=1, children=[Node(type=2, children=[])])]) # pragma: no cover

class MockSyms:# pragma: no cover
    atom = 1# pragma: no cover
    testlist_gexp = 2# pragma: no cover
    namedexpr_test = 3# pragma: no cover
# pragma: no cover
denylist = {attr for attr in MockSyms.__dict__.keys() if (not attr.startswith('__') or not attr.endswith('__'))}# pragma: no cover
syms = MockSyms() # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, node_type, children=None):# pragma: no cover
        self.type = node_type# pragma: no cover
        self.children = children if children else []# pragma: no cover
node = Node(node_type=syms.atom) # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    # For testing purposes, assume node always contains a single 'testlist_gexp' child# pragma: no cover
    return Node(syms.testlist_gexp, children=[Node(syms.namedexpr_test)]) if node.type == syms.atom else None # pragma: no cover

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
