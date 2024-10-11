from lib2to3.pytree import Leaf, Node # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover
from lib2to3.pgen2.token import DOUBLESTAR, LPAR, RPAR # pragma: no cover

node = type('Mock', (object,), {'children': ['_operator_mock', type('Mock', (object,), {'type': syms.power, 'children': [0, type('Mock', (object,), {'type': DOUBLESTAR}), 2], 'remove': lambda: 0})], 'insert_child': lambda index, value: None})() # pragma: no cover
self = type('Mock', (object,), {'visit_default': lambda node: None})() # pragma: no cover

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
