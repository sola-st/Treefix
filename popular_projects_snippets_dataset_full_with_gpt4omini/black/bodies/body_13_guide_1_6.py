import token # pragma: no cover
from typing import Any, List, Callable # pragma: no cover

class Preview:# pragma: no cover
    wrap_long_dict_values_in_parens = 'wrap' # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, children: List[Any]):# pragma: no cover
        self.children = children# pragma: no cover
        self.type = None # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self, mode):# pragma: no cover
        self.mode = mode# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'exit' # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma):# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node, child, visible): pass # pragma: no cover
children = [MockNode([]), MockNode([])]# pragma: no cover
children[0].type = token.COLON# pragma: no cover
children[1].children = [MockNode([])]# pragma: no cover
children[1].children[0].type = token.LPAR # pragma: no cover
node = MockNode(children) # pragma: no cover
self = Mock(mode=[Preview.wrap_long_dict_values_in_parens]) # pragma: no cover

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
