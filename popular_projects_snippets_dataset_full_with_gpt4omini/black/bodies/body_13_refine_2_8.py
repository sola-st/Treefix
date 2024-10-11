from typing import List # pragma: no cover
import token # pragma: no cover

class MockPreview: wrap_long_dict_values_in_parens = True # pragma: no cover
self = type('MockSelf', (object,), {'mode': [MockPreview.wrap_long_dict_values_in_parens]})() # pragma: no cover

from typing import List # pragma: no cover
import token # pragma: no cover

class Preview:# pragma: no cover
    wrap_long_dict_values_in_parens = True # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = [Preview.wrap_long_dict_values_in_parens]# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'default_visit_result' # pragma: no cover
class Child:# pragma: no cover
    def __init__(self, type, children):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children):# pragma: no cover
        self.children = children # pragma: no cover
node = Node([# pragma: no cover
    Child(token.COLON, []),# pragma: no cover
    Child('atom', [Child(token.LPAR, [])])# pragma: no cover
]) # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent=None, remove_brackets_around_comma=False):# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(parent, child, visible=True): pass # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if Preview.wrap_long_dict_values_in_parens in self.mode:
    _l_(5392)

    for i, child in enumerate(node.children):
        _l_(5391)

        if i == 0:
            _l_(5385)

            continue
            _l_(5384)
        if node.children[i - 1].type == token.COLON:
            _l_(5390)

            if child.type == syms.atom and child.children[0].type == token.LPAR:
                _l_(5389)

                if maybe_make_parens_invisible_in_atom(
                    child,
                    parent=node,
                    remove_brackets_around_comma=False,
                ):
                    _l_(5387)

                    wrap_in_parentheses(node, child, visible=False)
                    _l_(5386)
            else:
                wrap_in_parentheses(node, child, visible=False)
                _l_(5388)
aux = self.visit_default(node)
_l_(5393)
exit(aux)
