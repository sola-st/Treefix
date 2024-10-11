from dataclasses import dataclass # pragma: no cover
from typing import List # pragma: no cover

@dataclass # pragma: no cover
class Node: # pragma: no cover
    type: int # pragma: no cover
    children: List # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
node = Node(type=1, children=[]) # pragma: no cover
syms = type('syms', (object,), {'simple_stmt': 1, 'atom': 2}) # pragma: no cover
token = type('token', (object,), {'DOT': 1}) # pragma: no cover

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
