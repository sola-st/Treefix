from typing import List # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type, children: List['Node']):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children # pragma: no cover
class Leaf(Node):# pragma: no cover
    def __init__(self, token_type, value: str):# pragma: no cover
        super().__init__(token_type, [])# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
    def __eq__(self, other):# pragma: no cover
        return isinstance(other, Leaf) and self.type == other.type and self.value == other.value # pragma: no cover
class syms:# pragma: no cover
    simple_stmt = 1# pragma: no cover
    atom = 2 # pragma: no cover
class token:# pragma: no cover
    DOT = 3 # pragma: no cover
node = Node(syms.simple_stmt, [Node(syms.atom, [Leaf(token.DOT, '.'), Leaf(token.DOT, '.'), Leaf(token.DOT, '.')]), None]) # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type, children):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, token_type, value):# pragma: no cover
        self.token_type = token_type# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
    def __eq__(self, other):# pragma: no cover
        return isinstance(other, Leaf) and self.token_type == other.token_type and self.value == other.value # pragma: no cover
syms = type('syms', (object,), {'simple_stmt': 'simple_stmt', 'atom': 'atom'}) # pragma: no cover
token = type('token', (object,), {'DOT': 'DOT'}) # pragma: no cover
node = Node(type='simple_stmt', children=[Node(type='atom', children=[Leaf(token.DOT, '.'), Leaf(token.DOT, '.'), Leaf(token.DOT, '.')]), Leaf(token.DOT, '.')]) # pragma: no cover

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
