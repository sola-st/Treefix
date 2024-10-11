class Leaf: # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type; # pragma: no cover
        self.value = value; # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, children): # pragma: no cover
        self.children = children; # pragma: no cover
def wrap_in_parentheses(node, leaf): # pragma: no cover
    print(f'Wrapped {leaf.value} in parentheses') # pragma: no cover
def remove_await_parens(node): # pragma: no cover
    print('Removed redundant await parentheses') # pragma: no cover
class Preview: # pragma: no cover
    remove_redundant_parens = True # pragma: no cover
self = type('Mock', (object,), {'mode': [True]}) # pragma: no cover
aux = None # pragma: no cover

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
