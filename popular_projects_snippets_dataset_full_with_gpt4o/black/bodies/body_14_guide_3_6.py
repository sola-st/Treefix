import token # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover

class Preview: # pragma: no cover
    annotation_parens = 'parens_annotation' # pragma: no cover
 # pragma: no cover
Preview = Preview() # pragma: no cover
 # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.children = [MockChild(token.RARROW), MockChild(syms.atom, [MockChild(token.LPAR)])] # pragma: no cover
 # pragma: no cover
class MockChild: # pragma: no cover
    def __init__(self, type, children=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children or [] # pragma: no cover
 # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma=False): # pragma: no cover
    return True # pragma: no cover
 # pragma: no cover
def wrap_in_parentheses(node, child, visible=False): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, mode): # pragma: no cover
        self.mode = mode # pragma: no cover
    def visit_stmt(self, node, keywords={'def'}, parens=set()): # pragma: no cover
        return 'stmt_result' # pragma: no cover
    def line(self): # pragma: no cover
        return 'line_result' # pragma: no cover
    def visit(self, child): # pragma: no cover
        return 'visit_result' # pragma: no cover
 # pragma: no cover
self = MockSelf(mode={'parens_annotation'}) # pragma: no cover
node = MockNode() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Visit function definition."""
if Preview.annotation_parens not in self.mode:
    _l_(17554)

    aux = self.visit_stmt(node, keywords={"def"}, parens=set())
    _l_(17540)
    exit(aux)
else:
    aux = self.line()
    _l_(17541)
    exit(aux)

    # Remove redundant brackets around return type annotation.
    is_return_annotation = False
    _l_(17542)
    for child in node.children:
        _l_(17551)

        if child.type == token.RARROW:
            _l_(17550)

            is_return_annotation = True
            _l_(17543)
        elif is_return_annotation:
            _l_(17549)

            if child.type == syms.atom and child.children[0].type == token.LPAR:
                _l_(17547)

                if maybe_make_parens_invisible_in_atom(
                    child,
                    parent=node,
                    remove_brackets_around_comma=False,
                ):
                    _l_(17545)

                    wrap_in_parentheses(node, child, visible=False)
                    _l_(17544)
            else:
                wrap_in_parentheses(node, child, visible=False)
                _l_(17546)
            is_return_annotation = False
            _l_(17548)

    for child in node.children:
        _l_(17553)

        aux = self.visit(child)
        _l_(17552)
        exit(aux)
