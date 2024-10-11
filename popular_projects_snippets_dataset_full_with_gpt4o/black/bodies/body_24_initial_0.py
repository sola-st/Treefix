from typed_ast import ast3 as ast # pragma: no cover
from lib2to3.pgen2 import token # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover

node = type('MockNode', (object,), {'children': [Leaf(token.MINUS, '-'), Node(syms.power, [Leaf(token.NUMBER, '2'), Leaf(token.DOUBLESTAR, '**'), Leaf(token.NUMBER, '8')])], 'insert_child': lambda self, index, node: None})() # pragma: no cover
syms = type('MockSyms', (object,), {'power': 22, 'atom': 3}) # pragma: no cover
token = type('MockToken', (object,), {'DOUBLESTAR': 54, 'LPAR': 7, 'RPAR': 8, 'MINUS': 11, 'NUMBER': 2}) # pragma: no cover
Leaf = Leaf # pragma: no cover
Node = Node # pragma: no cover
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
