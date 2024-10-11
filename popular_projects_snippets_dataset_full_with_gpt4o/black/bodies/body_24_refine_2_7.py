from typing import List # pragma: no cover
class Leaf: pass # pragma: no cover
class Node: pass # pragma: no cover

node = type('MockNode', (object,), {'children': [Leaf(), Node()], 'insert_child': lambda self, index, node: None})() # pragma: no cover
syms = type('MockSyms', (object,), {'power': 'power', 'atom': 'atom'})() # pragma: no cover
token = type('MockToken', (object,), {'DOUBLESTAR': '**', 'LPAR': '(', 'RPAR': ')' }) # pragma: no cover
Leaf = type('MockLeaf', (object,), {'__init__': lambda self, type, value: None}) # pragma: no cover
Node = type('MockNode2', (object,), {'__init__': lambda self, type, children: None}) # pragma: no cover
self = type('MockSelf', (object,), {'visit_default': lambda self, node: None})() # pragma: no cover

from typing import List # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover
import token # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover

node = type('MockNode', (object,), {'children': [Leaf(token.MINUS, '-'), Node(syms.power, [Leaf(token.NUMBER, '2'), Leaf(token.DOUBLESTAR, '**'), Leaf(token.NUMBER, '8')])], 'insert_child': lambda self, index, node: None})() # pragma: no cover
syms = type('MockSyms', (object,), {'power': syms.power, 'atom': syms.atom})() # pragma: no cover
token = type('MockToken', (object,), {'DOUBLESTAR': token.DOUBLESTAR, 'LPAR': token.LPAR, 'RPAR': token.RPAR, 'MINUS': token.MINUS, 'NUMBER': token.NUMBER}) # pragma: no cover
Leaf = Leaf # pragma: no cover
Node = type('MockNodeType', (Node,), {'__init__': lambda self, type, children: super(Node, self).__init__(type, children)}) # pragma: no cover
Node(syms.power, []).type = syms.power # pragma: no cover
self = type('MockSelf', (object,), {'visit_default': lambda self, node: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Force parentheses between a unary op and a binary power:

        -2 ** 8 -> -(2 ** 8)
        """
_operator, operand = node.children
_l_(16392)
if (
    operand.type == syms.power
    and len(operand.children) == 3
    and operand.children[1].type == token.DOUBLESTAR
):
    _l_(16397)

    lpar = Leaf(token.LPAR, "(")
    _l_(16393)
    rpar = Leaf(token.RPAR, ")")
    _l_(16394)
    index = operand.remove() or 0
    _l_(16395)
    node.insert_child(index, Node(syms.atom, [lpar, operand, rpar]))
    _l_(16396)
aux = self.visit_default(node)
_l_(16398)
exit(aux)
