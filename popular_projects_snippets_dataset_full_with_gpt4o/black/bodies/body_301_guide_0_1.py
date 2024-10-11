from typing import Any # pragma: no cover

token = type('MockToken', (object,), {'DOT': '.'})() # pragma: no cover
Leaf = lambda x, y: (x, y) # pragma: no cover
Node = type('Node', (object,), {'type': Any, 'children': list}) # pragma: no cover
syms = type('MockSyms', (object,), {'simple_stmt': 'simple_statement', 'atom': 'atom'})() # pragma: no cover
node = Node() # pragma: no cover
node.type = syms.simple_stmt # pragma: no cover
node.children = [Node() for _ in range(2)] # pragma: no cover
node.children[0].type = syms.atom # pragma: no cover
node.children[0].children = [Leaf(token.DOT, '.'), Leaf(token.DOT, '.'), Leaf(token.DOT, '.')] # pragma: no cover

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
