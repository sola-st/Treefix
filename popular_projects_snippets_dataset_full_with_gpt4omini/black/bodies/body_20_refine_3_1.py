from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, value: str, leaf_type: Any):# pragma: no cover
        self.value = value# pragma: no cover
        self.type = leaf_type # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List[Leaf]):# pragma: no cover
        self.children = children # pragma: no cover
wrap_in_parentheses = lambda node, leaf: print(f'Wrapping {leaf.value} in parentheses.') # pragma: no cover
class Preview:# pragma: no cover
    remove_redundant_parens = True # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = Preview.remove_redundant_parens# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'Visited default node'# pragma: no cover
self = MockSelf() # pragma: no cover
remove_await_parens = lambda node: print('Removing await parentheses.') # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, value: str, leaf_type: Any):# pragma: no cover
        self.value = value# pragma: no cover
        self.type = leaf_type # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List[Leaf]):# pragma: no cover
        self.children = children # pragma: no cover
wrap_in_parentheses = lambda node, leaf: print(f'Wrapping {leaf.value} in parentheses.') # pragma: no cover
class Preview:# pragma: no cover
    remove_redundant_parens = True # pragma: no cover
class Self:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = ['remove_redundant_parens']# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 0# pragma: no cover
self = Self() # pragma: no cover
remove_await_parens = lambda node: print('Removing await parentheses.') # pragma: no cover

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
