from collections import namedtuple # pragma: no cover

Node = namedtuple('Node', ['type', 'children']) # pragma: no cover
Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
syms = type('MockSymbols', (), {'simple_stmt': 'simple_stmt', 'atom': 'atom'})() # pragma: no cover
token = type('MockToken', (), {'DOT': 'DOT'})() # pragma: no cover
node = Node(type='simple_stmt', children=[Node(type='atom', children=[Leaf(type='DOT', value='.'), Leaf(type='DOT', value='.'), Leaf(type='DOT', value='.')])]) # pragma: no cover

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
