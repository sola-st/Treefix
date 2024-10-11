from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type_: int, value: str):# pragma: no cover
        self.type = type_# pragma: no cover
        self.value = value # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, type_: int, children: List[Any]):# pragma: no cover
        self.type = type_# pragma: no cover
        self.children = children# pragma: no cover
    def insert_child(self, index: int, child: Any):# pragma: no cover
        self.children.insert(index, child)# pragma: no cover
    def remove(self):# pragma: no cover
        return self.children.pop() if self.children else None # pragma: no cover
node = Node(0, [None, Node(1, [None, None, None]), None]) # pragma: no cover
syms = type('Mock', (object,), {'power': 1, 'atom': 2})() # pragma: no cover
token = type('Mock', (object,), {'DOUBLESTAR': 3, 'LPAR': 4, 'RPAR': 5})() # pragma: no cover
self = type('Mock', (object,), {'visit_default': lambda self, node: None})() # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type_: int, value: str):# pragma: no cover
        self.type = type_# pragma: no cover
        self.value = value # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, type_: int, children: List[Any]):# pragma: no cover
        self.type = type_# pragma: no cover
        self.children = children# pragma: no cover
    def insert_child(self, index: int, child: Any):# pragma: no cover
        self.children.insert(index, child)# pragma: no cover
    def remove(self):# pragma: no cover
        return self.children.pop() if self.children else None # pragma: no cover
syms = type('Mock', (object,), {'power': 1, 'atom': 2})() # pragma: no cover
token = type('Mock', (object,), {'DOUBLESTAR': 3, 'LPAR': 4, 'RPAR': 5})() # pragma: no cover
operator_node = Leaf(0, None)  # Placeholder for unary operator (e.g., '-') # pragma: no cover
operand_node = Node(syms.power, [Leaf('NUM', '2'), Leaf(token.DOUBLESTAR, '**'), Leaf('NUM', '8')]) # pragma: no cover
node = Node(0, [operator_node, operand_node]) # pragma: no cover
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
