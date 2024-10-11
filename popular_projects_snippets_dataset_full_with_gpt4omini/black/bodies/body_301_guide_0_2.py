from typing import List, Union # pragma: no cover
from collections import namedtuple # pragma: no cover

Node = type('Node', (object,), {}) # pragma: no cover
Leaf = type('Leaf', (object,), {}) # pragma: no cover
syms = type('syms', (object,), {'simple_stmt': 1, 'atom': 2}) # pragma: no cover
token = type('token', (object,), {'DOT': 1}) # pragma: no cover
node = Node() # pragma: no cover
node.type = syms.simple_stmt # pragma: no cover
node.children = [Node(), Node()] # pragma: no cover
child = node.children[0] # pragma: no cover
child.type = syms.atom # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` is a simple statement containing an ellipsis."""
if not isinstance(node, Node) or node.type != syms.simple_stmt:
    _l_(7917)

    aux = False
    _l_(7916)
    exit(aux)

if len(node.children) != 2:
    _l_(7919)

    aux = False
    _l_(7918)
    exit(aux)

child = node.children[0]
_l_(7920)
aux = (
    child.type == syms.atom
    and len(child.children) == 3
    and all(leaf == Leaf(token.DOT, ".") for leaf in child.children)
)
_l_(7921)
exit(aux)
