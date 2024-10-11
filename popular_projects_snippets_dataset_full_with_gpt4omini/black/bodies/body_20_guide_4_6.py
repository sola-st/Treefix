import token # pragma: no cover

class Leaf: pass # pragma: no cover
class Node: pass # pragma: no cover
def wrap_in_parentheses(node, leaf): print(f'Wrapping: {leaf.value}') # pragma: no cover
def remove_await_parens(node): print('Removing await parens') # pragma: no cover
Preview = type('MockPreview', (object,), {'remove_redundant_parens': True})() # pragma: no cover
node = Node() # pragma: no cover
leaf1 = Leaf(); leaf1.value = '42'; leaf1.type = token.NUMBER # pragma: no cover
self = type('MockSelf', (object,), {'mode': [Preview.remove_redundant_parens], 'visit_default': lambda node: 'done'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
for idx, leaf in enumerate(node.children[:-1]):
    _l_(8198)

    next_leaf = node.children[idx + 1]
    _l_(8192)

    if not isinstance(leaf, Leaf):
        _l_(8194)

        continue
        _l_(8193)

    value = leaf.value.lower()
    _l_(8195)
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
        _l_(8197)

        wrap_in_parentheses(node, leaf)
        _l_(8196)

if Preview.remove_redundant_parens in self.mode:
    _l_(8200)

    remove_await_parens(node)
    _l_(8199)
aux = self.visit_default(node)
_l_(8201)

exit(aux)
