from typing import List # pragma: no cover
from typing import Union # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type_: int, children: List[Union['Node', 'Leaf']]):# pragma: no cover
        self.type = type_# pragma: no cover
        self.children = children # pragma: no cover
syms = type('syms', (object,), {'simple_stmt': 1, 'atom': 2}) # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, token_type: int, value: str):# pragma: no cover
        self.token_type = token_type# pragma: no cover
        self.value = value # pragma: no cover
token = type('token', (object,), {'DOT': 1}) # pragma: no cover
child1 = Leaf(token.DOT, '.') # pragma: no cover
child2 = Leaf(token.DOT, '.') # pragma: no cover
child3 = Leaf(token.DOT, '.') # pragma: no cover
atom_node = Node(syms.atom, [child1, child2, child3]) # pragma: no cover
node = Node(syms.simple_stmt, [atom_node, None]) # pragma: no cover

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
