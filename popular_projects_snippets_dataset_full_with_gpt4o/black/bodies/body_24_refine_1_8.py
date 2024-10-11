from typing import Any, List # pragma: no cover
from lib2to3.pytree import Leaf, Node # pragma: no cover
from lib2to3.fixer_util import Node # pragma: no cover
import token # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover

syms = type('Mock', (object,), {'power': 277, 'atom': 270}) # pragma: no cover
token = type('Mock', (object,), {'DOUBLESTAR': 55, 'LPAR': 7, 'RPAR': 8}) # pragma: no cover
Leaf = Leaf # pragma: no cover
Node = Node # pragma: no cover
self = type('Mock', (object,), {'visit_default': lambda self, node: None})() # pragma: no cover

from lib2to3.pytree import Leaf, Node # pragma: no cover
import token # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover

syms = type('Mock', (object,), {'power': 277, 'atom': 270}) # pragma: no cover
token = type('Mock', (object,), {'DOUBLESTAR': 55, 'LPAR': 7, 'RPAR': 8, 'NUMBER': 2}) # pragma: no cover
Leaf = Leaf # pragma: no cover
Node = Node # pragma: no cover
self = type('Mock', (object,), {'visit_default': lambda self, node: None})() # pragma: no cover

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
