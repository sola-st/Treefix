import token # pragma: no cover
from typing import List # pragma: no cover

class syms: # pragma: no cover
    trailer = 'trailer' # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Trailer: # pragma: no cover
    def __init__(self, type, children): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, children: List): # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
def wrap_in_parentheses(node, leaf): # pragma: no cover
    print(f'Wrapped {leaf.value} in parentheses') # pragma: no cover
 # pragma: no cover
def remove_await_parens(node): # pragma: no cover
    print('Removed redundant parentheses') # pragma: no cover
 # pragma: no cover
class Preview: # pragma: no cover
    remove_redundant_parens = 'remove_redundant_parens' # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'mode': [Preview.remove_redundant_parens], # pragma: no cover
    'visit_default': lambda self, node: 'default_visit_result' # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
non_leaf = 'Not a leaf object' # pragma: no cover
# Trigger the 'continue' path # pragma: no cover
valid_leaf = Leaf(type=token.NUMBER, value='123') # pragma: no cover
# Valid leaf that meets the conditions # pragma: no cover
dot_leaf = Leaf(type=token.DOT, value='.') # pragma: no cover
# Dot leaf for trailer # pragma: no cover
trailer = Trailer(type=syms.trailer, children=[dot_leaf]) # pragma: no cover
# Trailer containing dot leaf # pragma: no cover
node = Node(children=[non_leaf, valid_leaf, trailer]) # pragma: no cover
# Node with necessary children # pragma: no cover

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
