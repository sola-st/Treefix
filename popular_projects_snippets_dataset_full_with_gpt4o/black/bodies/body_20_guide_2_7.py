import token # pragma: no cover
from dataclasses import dataclass # pragma: no cover
from typing import List # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Trailer: # pragma: no cover
    type: int # pragma: no cover
    children: List[Leaf] # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Node: # pragma: no cover
    children: List[object] # pragma: no cover
 # pragma: no cover
class syms: # pragma: no cover
    trailer = 1 # pragma: no cover
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
class Self: # pragma: no cover
    mode = [Preview.remove_redundant_parens] # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        return 'Default visit executed' # pragma: no cover
 # pragma: no cover
# Create nodes and leaf instances to test the conditions # pragma: no cover
leaf1 = Leaf(type=token.NUMBER, value='123') # pragma: no cover
dot_leaf = Leaf(type=token.DOT, value='.') # pragma: no cover
trailer = Trailer(type=syms.trailer, children=[dot_leaf]) # pragma: no cover
node = Node(children=[leaf1, trailer]) # pragma: no cover
self = Self() # pragma: no cover
# Execute the snippet # pragma: no cover
for idx, leaf in enumerate(node.children[:-1]): # pragma: no cover
    next_leaf = node.children[idx + 1] # pragma: no cover
    if not isinstance(leaf, Leaf): # pragma: no cover
        continue # pragma: no cover
    value = leaf.value.lower() # pragma: no cover
    if ( # pragma: no cover
        leaf.type == token.NUMBER # pragma: no cover
        and next_leaf.type == syms.trailer # pragma: no cover
        and next_leaf.children[0].type == token.DOT # pragma: no cover
        and not value.startswith(('0x', '0b', '0o')) # pragma: no cover
        and 'j' not in value # pragma: no cover
    ): # pragma: no cover
        wrap_in_parentheses(node, leaf) # pragma: no cover
if Preview.remove_redundant_parens in self.mode: # pragma: no cover
    remove_await_parens(node) # pragma: no cover
aux = self.visit_default(node) # pragma: no cover
print(aux) # pragma: no cover

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
