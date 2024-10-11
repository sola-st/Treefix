from typing import List # pragma: no cover
from collections import namedtuple # pragma: no cover

Node = namedtuple('Node', ['children', 'insert_child']) # pragma: no cover
Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
token = type('token', (), {'DOUBLESTAR': 1, 'LPAR': 2, 'RPAR': 3})() # pragma: no cover
syms = type('syms', (), {'power': 4, 'atom': 5})() # pragma: no cover
node = Node(children=[None, Leaf(0, 2), None], insert_child=lambda index, child: None) # pragma: no cover

from typing import List # pragma: no cover
from collections import namedtuple # pragma: no cover

Node = namedtuple('Node', ['children', 'insert_child']) # pragma: no cover
Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
token = type('token', (), {'DOUBLESTAR': 1, 'LPAR': 2, 'RPAR': 3})() # pragma: no cover
syms = type('syms', (), {'power': 4, 'atom': 5})() # pragma: no cover
operand = Leaf(type=syms.power, value=2) # pragma: no cover
operator = Leaf(type=0, value=-2) # pragma: no cover
node = Node(children=[operator, operand], insert_child=lambda index, child: None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Force parentheses between a unary op and a binary power:

        -2 ** 8 -> -(2 ** 8)
        """
_operator, operand = node.children
_l_(4751)
if (
    operand.type == syms.power
    and len(operand.children) == 3
    and operand.children[1].type == token.DOUBLESTAR
):
    _l_(4756)

    lpar = Leaf(token.LPAR, "(")
    _l_(4752)
    rpar = Leaf(token.RPAR, ")")
    _l_(4753)
    index = operand.remove() or 0
    _l_(4754)
    node.insert_child(index, Node(syms.atom, [lpar, operand, rpar]))
    _l_(4755)
aux = self.visit_default(node)
_l_(4757)
exit(aux)
