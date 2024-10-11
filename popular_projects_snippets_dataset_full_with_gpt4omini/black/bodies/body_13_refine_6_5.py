from typing import List, Any # pragma: no cover
import token # pragma: no cover
from itertools import chain # pragma: no cover

class Preview: wrap_long_dict_values_in_parens = 'some_value' # pragma: no cover
self = type('MockSelf', (object,), {'mode': ['some_mode']})() # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 'atom_value'})() # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: True # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Preview:# pragma: no cover
    wrap_long_dict_values_in_parens = True # pragma: no cover
class MockSelf:# pragma: no cover
    mode = [Preview.wrap_long_dict_values_in_parens]# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'default_visit_result'# pragma: no cover
self = MockSelf() # pragma: no cover
class MockChild:# pragma: no cover
    def __init__(self, type, children=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children if children is not None else [] # pragma: no cover
token = type('MockToken', (), {'COLON': 'COLON', 'LPAR': 'LPAR'})() # pragma: no cover
syms = type('MockSyms', (), {'atom': 'atom'})() # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent=None, remove_brackets_around_comma=False):# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node, child, visible=False):# pragma: no cover
    pass # pragma: no cover

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
