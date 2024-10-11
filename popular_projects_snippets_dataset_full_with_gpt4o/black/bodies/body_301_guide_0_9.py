from typing import List # pragma: no cover
from collections import namedtuple # pragma: no cover

token = type("Mock", (object,), {"DOT": "."}) # pragma: no cover
Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
syms = type("Mock", (object,), {"simple_stmt": "simple_stmt", "atom": "atom"}) # pragma: no cover
Node = namedtuple('Node', ['type', 'children']) # pragma: no cover
node = Node(type=syms.simple_stmt, children=[Node(type=syms.atom, children=[Leaf(token.DOT, '.'),Leaf(token.DOT, '.'),Leaf(token.DOT, '.')]), "other_child"]) # pragma: no cover

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
