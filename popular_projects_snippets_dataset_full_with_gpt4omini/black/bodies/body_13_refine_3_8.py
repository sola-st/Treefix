from typing import List, Dict # pragma: no cover
import token # pragma: no cover

class MockPreview:# pragma: no cover
    wrap_long_dict_values_in_parens = True# pragma: no cover
# pragma: no cover
Preview = MockPreview() # pragma: no cover
class MockSelf:# pragma: no cover
    mode = [True]# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockNode:# pragma: no cover
    class Child:# pragma: no cover
        def __init__(self, child_type, children):# pragma: no cover
            self.type = child_type# pragma: no cover
            self.children = children# pragma: no cover
node = MockNode() # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma):# pragma: no cover
    return True# pragma: no cover
# pragma: no cover
maybe_make_parens_invisible_in_atom = maybe_make_parens_invisible_in_atom # pragma: no cover
def wrap_in_parentheses(node, child, visible):# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
wrap_in_parentheses = wrap_in_parentheses # pragma: no cover
def mock_visit_default(node):# pragma: no cover
    return 'default'# pragma: no cover
# pragma: no cover
self.visit_default = mock_visit_default # pragma: no cover

from typing import List, Dict, Any # pragma: no cover

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
