from typing import List, Any # pragma: no cover
import token # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.children = [] # pragma: no cover
class Mock:# pragma: no cover
    mode = [True]# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return None # pragma: no cover
self = Mock() # pragma: no cover
node = MockNode() # pragma: no cover
node.children = [MockNode(), MockNode(), MockNode()] # pragma: no cover
node.children[0].type = token.COLON# pragma: no cover
node.children[1].children = [MockNode()] # pragma: no cover
node.children[1].children[0].type = token.LPAR # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma):# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node, child, visible):# pragma: no cover
    pass # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Preview:# pragma: no cover
    wrap_long_dict_values_in_parens = 'wrap_long_dict_values_in_parens' # pragma: no cover
self = type('MockSelf', (object,), {'mode': [Preview.wrap_long_dict_values_in_parens]})() # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, children=None):# pragma: no cover
        self.children = children if children is not None else [] # pragma: no cover
node = MockNode() # pragma: no cover
node.children.append(MockNode())  # Placeholder for index 0# pragma: no cover
 # pragma: no cover
node.children.append(MockNode())  # Placeholder for index 1# pragma: no cover
 # pragma: no cover
node.children[0].type = token.COLON# pragma: no cover
 # pragma: no cover
node.children[1].children.append(MockNode())# pragma: no cover
 # pragma: no cover
node.children[1].children[0].type = token.LPAR# pragma: no cover
 # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent=None, remove_brackets_around_comma=False):# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node, child, visible): pass # pragma: no cover

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
