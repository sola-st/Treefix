import token # pragma: no cover
from typing import List, Any # pragma: no cover

class MockNode:  # represents a mock of the node structure# pragma: no cover
    def __init__(self, children: List[Any], node_type: str):# pragma: no cover
        self.children = children# pragma: no cover
        self.type = node_type # pragma: no cover
class MockMode:# pragma: no cover
    def __contains__(self, item): return item == 'wrap_long_dict_values_in_parens' # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma):# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node, child, visible): pass # pragma: no cover
self = type('MockSelf', (object,), {'mode': MockMode(), 'visit_default': lambda node: None})() # pragma: no cover

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
