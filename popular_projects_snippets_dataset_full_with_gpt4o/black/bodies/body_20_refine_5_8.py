from typing import List, Any # pragma: no cover

node = type('Mock', (object,), {'children': [type('MockLeaf', (object,), {'value': '123', 'type': 'NUMBER'})(), type('MockLeaf', (object,), {'children': [type('MockDot', (object,), {'type': 'DOT'})()], 'type': 'trailer'})()]})() # pragma: no cover
Leaf = type('MockLeaf', (object,), {}) # pragma: no cover
token = type('MockToken', (object,), {'NUMBER': 'NUMBER', 'DOT': 'DOT'}) # pragma: no cover
syms = type('MockSyms', (object,), {'trailer': 'trailer'}) # pragma: no cover
def wrap_in_parentheses(node: Any, leaf: Any) -> None: pass # pragma: no cover
Preview = type('MockPreview', (object,), {'remove_redundant_parens': 'remove_redundant_parens'}) # pragma: no cover
self = type('MockSelf', (object,), {'mode': ['remove_redundant_parens'], 'visit_default': lambda node: None})() # pragma: no cover
def remove_await_parens(node: Any) -> None: pass # pragma: no cover

from typing import List, Any # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, leaf_type: int, value: str):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.value = value # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List[Any]):# pragma: no cover
        self.children = children # pragma: no cover
token = type('token', (object,), {'NUMBER': 2, 'DOT': 1}) # pragma: no cover
syms = type('syms', (object,), {'trailer': 'trailer'}) # pragma: no cover
def wrap_in_parentheses(node: Any, leaf: Leaf):# pragma: no cover
    pass # pragma: no cover
Preview = type('Preview', (object,), {'remove_redundant_parens': 'remove_redundant_parens'}) # pragma: no cover
class SelfMock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = ['remove_redundant_parens']# pragma: no cover
    def visit_default(self, node: Any):# pragma: no cover
        pass # pragma: no cover
self = SelfMock() # pragma: no cover
def remove_await_parens(node: Any):# pragma: no cover
    pass # pragma: no cover

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
