from collections import namedtuple # pragma: no cover
import token # pragma: no cover
class Node: pass # pragma: no cover
class Leaf: pass # pragma: no cover

Node = namedtuple('Node', ['children']) # pragma: no cover
node = Node(children=[Node(children=[]), Node(children=[None, None, None])]) # pragma: no cover
syms = type('Mock', (object,), {'power': 'power', 'atom': 'atom'})() # pragma: no cover
token = type('Mock', (object,), {'DOUBLESTAR': 'DOUBLESTAR', 'LPAR': 'LPAR', 'RPAR': 'RPAR'})() # pragma: no cover
Leaf = lambda type, value: {'type': type, 'value': value} # pragma: no cover
self = type('Mock', (object,), {'visit_default': lambda self, node: None})() # pragma: no cover

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
