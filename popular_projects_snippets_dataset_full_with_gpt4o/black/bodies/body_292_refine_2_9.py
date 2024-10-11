from typing import List # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type, children=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children if children else []# pragma: no cover
syms = type('Mock', (object,), {'atom': 1, 'testlist_gexp': 2, 'namedexpr_test': 3}) # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    return node if len(node.children) == 1 else None # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type, children=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children if children else []# pragma: no cover
 # pragma: no cover
syms = type('Mock', (object,), {'atom': 1, 'testlist_gexp': 2, 'namedexpr_test': 3}) # pragma: no cover
node = Node(type=syms.atom, children=[Node(type=syms.testlist_gexp, children=[Node(type=syms.namedexpr_test)])]) # pragma: no cover
def unwrap_singleton_parenthesis(node):# pragma: no cover
    if len(node.children) == 1:# pragma: no cover
        return node.children[0]# pragma: no cover
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
