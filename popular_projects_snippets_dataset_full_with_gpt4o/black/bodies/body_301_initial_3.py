from typing import List # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class Node: # pragma: no cover
    def __init__(self, type: str, children: List): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, token_type: str, value: str): # pragma: no cover
        self.token_type = token_type # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
token = SimpleNamespace(DOT='DOT') # pragma: no cover
syms = SimpleNamespace(simple_stmt='simple_stmt', atom='atom') # pragma: no cover
 # pragma: no cover
node = Node(syms.simple_stmt, [ # pragma: no cover
    Node(syms.atom, [Leaf(token.DOT, '.'), Leaf(token.DOT, '.'), Leaf(token.DOT, '.')]), # pragma: no cover
    None # pragma: no cover
]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` is a simple statement containing an ellipsis."""
if not isinstance(node, Node) or node.type != syms.simple_stmt:
    _l_(19684)

    aux = False
    _l_(19683)
    exit(aux)

if len(node.children) != 2:
    _l_(19686)

    aux = False
    _l_(19685)
    exit(aux)

child = node.children[0]
_l_(19687)
aux = (
    child.type == syms.atom
    and len(child.children) == 3
    and all(leaf == Leaf(token.DOT, ".") for leaf in child.children)
)
_l_(19688)
exit(aux)
