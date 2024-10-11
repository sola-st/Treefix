import token # pragma: no cover
from collections import namedtuple # pragma: no cover

class MockNode: pass # pragma: no cover
MockNode.children = [] # pragma: no cover
MockNode.type = None # pragma: no cover
class Mock: pass # pragma: no cover
node = MockNode() # pragma: no cover
node.children.append(MockNode()) # pragma: no cover
node.children.append(MockNode()) # pragma: no cover
node.children[0].type = token.COLON # pragma: no cover
node.children[1].children = [MockNode()] # pragma: no cover
node.children[1].children[0].type = token.LPAR # pragma: no cover
self = Mock() # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma): return True # pragma: no cover
def wrap_in_parentheses(node, child, visible): pass # pragma: no cover
def visit_default(node): return None # pragma: no cover
self.visit_default = visit_default # pragma: no cover

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
