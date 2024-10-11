from typing import List, Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover

node = type('Mock', (object,), {})() # pragma: no cover
node.children = [type('Leaf', (object,), {'type': 1, 'value': str(i)})() for i in range(1, 20)] # pragma: no cover
Leaf = type('Leaf', (object,), {'type': int, 'value': str}) # pragma: no cover
token = type('Mock', (object,), {'NUMBER': 1, 'DOT': 2}) # pragma: no cover
syms = type('Mock', (object,), {'trailer': 3}) # pragma: no cover
wrap_in_parentheses = lambda node, leaf: None # pragma: no cover
Preview = type('Mock', (object,), {'remove_redundant_parens': 4}) # pragma: no cover
self = type('Mock', (object,), {'mode': [4], 'visit_default': lambda self, node: None, 'remove_await_parens': lambda node: None})() # pragma: no cover

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
