import tokenize # pragma: no cover

class syms: power = 'power'; atom = 'atom' # pragma: no cover
class token: DOUBLESTAR = '**'; LPAR = '('; RPAR = ')' # pragma: no cover
self = type('MockSelf', (), {'visit_default': lambda self, node: None})() # pragma: no cover

from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
Node = namedtuple('Node', ['children', 'insert_child']) # pragma: no cover
class syms: power = 'power'; atom = 'atom' # pragma: no cover
class token: DOUBLESTAR = 1; LPAR = 2; RPAR = 3 # pragma: no cover
operator_leaf = Leaf(token.DOUBLESTAR, '**') # pragma: no cover
self = type('MockSelf', (), {'visit_default': lambda self, node: node})() # pragma: no cover

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
