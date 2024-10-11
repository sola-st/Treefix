import token # pragma: no cover

node = type('MockNode', (object,), {'children': [type('MockLeaf', (object,), {'type': token.NUMBER, 'value': '12'}), type('MockTrailer', (object,), {'type': token.DOT, 'children': [type('MockDot', (object,), {'type': token.DOT})]})]})() # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, value: None}) # pragma: no cover
syms = type('MockSyms', (object,), {'trailer': type('MockTrailer', (object,), {})})() # pragma: no cover
wrap_in_parentheses = lambda node, leaf: None # pragma: no cover
Preview = type('Preview', (object,), {'remove_redundant_parens': 'remove_redundant_parens'}) # pragma: no cover
self = type('Self', (object,), {'mode': ['remove_redundant_parens'], 'visit_default': lambda node: None, 'visit_node': lambda self, node: None})() # pragma: no cover
remove_await_parens = lambda node: None # pragma: no cover

import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, leaf_type, value):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.value = value # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children):# pragma: no cover
        self.children = children # pragma: no cover
syms = type('MockSyms', (object,), {'trailer': 'trailer'}) # pragma: no cover
def wrap_in_parentheses(node, leaf):# pragma: no cover
    pass # pragma: no cover
class Preview:# pragma: no cover
    remove_redundant_parens = 'remove_redundant_parens' # pragma: no cover
class Self:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = [Preview.remove_redundant_parens]# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 0 # pragma: no cover
def remove_await_parens(node):# pragma: no cover
    pass # pragma: no cover
node = Node([# pragma: no cover
    Leaf(token.NUMBER, '123'),# pragma: no cover
    Node([Leaf(token.DOT, '.')])# pragma: no cover
]) # pragma: no cover
self = Self() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
for idx, leaf in enumerate(node.children[:-1]):
    _l_(19653)

    next_leaf = node.children[idx + 1]
    _l_(19647)

    if not isinstance(leaf, Leaf):
        _l_(19649)

        continue
        _l_(19648)

    value = leaf.value.lower()
    _l_(19650)
    if (
        leaf.type == token.NUMBER
        and next_leaf.type == syms.trailer
        # Ensure that we are in an attribute trailer
        and next_leaf.children[0].type == token.DOT
        # It shouldn't wrap hexadecimal, binary and octal literals
        and not value.startswith(("0x", "0b", "0o"))
        # It shouldn't wrap complex literals
        and "j" not in value
    ):
        _l_(19652)

        wrap_in_parentheses(node, leaf)
        _l_(19651)

if Preview.remove_redundant_parens in self.mode:
    _l_(19655)

    remove_await_parens(node)
    _l_(19654)
aux = self.visit_default(node)
_l_(19656)

exit(aux)
