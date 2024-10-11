from typing import List, Any # pragma: no cover
from types import ModuleType # pragma: no cover
import token # pragma: no cover

type('Leaf', (object,), {'__init__': lambda self, tok_type, value: setattr(self, 'tok_type', tok_type) or setattr(self, 'value', value) or None}) # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, tok_type, value: setattr(self, 'tok_type', tok_type) or setattr(self, 'value', value) or None}) # pragma: no cover
type('Node', (object,), {'__init__': lambda self, type, children: setattr(self, 'type', type) or setattr(self, 'children', children) or None}) # pragma: no cover
Node = type('Node', (object,), {'__init__': lambda self, type, children: setattr(self, 'type', type) or setattr(self, 'children', children) or None}) # pragma: no cover
type('Mock', (object,), {'simple_stmt': 'simple_stmt'}) # pragma: no cover
syms = type('Mock', (object,), {'simple_stmt': 'simple_stmt'}) # pragma: no cover
node = Node(syms.simple_stmt, [Leaf(token.DOT, '.'), Leaf(token.DOT, '.')]) # pragma: no cover

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
