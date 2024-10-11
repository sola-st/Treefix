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

node = type('MockNode', (object,), {'children': [Leaf(1, '-'), type('MockNodeChild', (object,), {'type': 'power', 'children': [Leaf(1, '2'), Leaf(1, '**'), Leaf(1, '8')], 'remove': lambda self: 0})()], 'insert_child': lambda self, index, node: None})() # pragma: no cover
syms = type('MockSyms', (object,), {'power': 'power', 'atom': 'atom'})() # pragma: no cover
token = type('MockToken', (object,), {'DOUBLESTAR': '**', 'LPAR': '(', 'RPAR': ')' }) # pragma: no cover
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
