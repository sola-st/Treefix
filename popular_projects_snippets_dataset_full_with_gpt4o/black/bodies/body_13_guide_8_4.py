import token # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover

class Preview: # pragma: no cover
    wrap_long_dict_values_in_parens = 1 # pragma: no cover
 # pragma: no cover
class MockChild: # pragma: no cover
    def __init__(self, type, children=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children if children is not None else [] # pragma: no cover
 # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.children = [ # pragma: no cover
            MockChild(token.COLON), # pragma: no cover
            MockChild(syms.atom, [MockChild(type=token.LPAR)]), # pragma: no cover
            MockChild(syms.atom, [MockChild(type=token.LPAR)]), # pragma: no cover
        ] # pragma: no cover
 # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma=False): # pragma: no cover
    return False  # Ensure this returns False to hit the uncovered path in `else` block # pragma: no cover
 # pragma: no cover
def wrap_in_parentheses(node, child, visible=False): # pragma: no cover
    print(f'Wrapped {child} in parentheses (visible={visible})') # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.mode = [Preview.wrap_long_dict_values_in_parens] # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        return 'aux_value' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
node = MockNode() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if Preview.wrap_long_dict_values_in_parens in self.mode:
    _l_(16886)

    for i, child in enumerate(node.children):
        _l_(16885)

        if i == 0:
            _l_(16879)

            continue
            _l_(16878)
        if node.children[i - 1].type == token.COLON:
            _l_(16884)

            if child.type == syms.atom and child.children[0].type == token.LPAR:
                _l_(16883)

                if maybe_make_parens_invisible_in_atom(
                    child,
                    parent=node,
                    remove_brackets_around_comma=False,
                ):
                    _l_(16881)

                    wrap_in_parentheses(node, child, visible=False)
                    _l_(16880)
            else:
                wrap_in_parentheses(node, child, visible=False)
                _l_(16882)
aux = self.visit_default(node)
_l_(16887)
exit(aux)
