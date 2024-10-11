from typing import Any, Dict, Set, List # pragma: no cover

class MockPreview:# pragma: no cover
    annotation_parens = '()'# pragma: no cover
# pragma: no cover
Preview = MockPreview() # pragma: no cover
class MockSelf:# pragma: no cover
    mode = 'some_mode'# pragma: no cover
    def visit_stmt(self, node, keywords, parens):# pragma: no cover
        return 0# pragma: no cover
    def line(self):# pragma: no cover
        return 1# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 0# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, children):# pragma: no cover
        self.children = children# pragma: no cover
class MockToken:# pragma: no cover
    RARROW = 'RARROW'# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
# pragma: no cover
token = MockToken() # pragma: no cover
class MockSyms:# pragma: no cover
    atom = 'atom'# pragma: no cover
# pragma: no cover
syms = MockSyms() # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma):# pragma: no cover
    return True# pragma: no cover
 # pragma: no cover
def wrap_in_parentheses(node, child, visible):# pragma: no cover
    pass # pragma: no cover

from typing import List # pragma: no cover

class MockPreview:# pragma: no cover
    annotation_parens = '()'# pragma: no cover
# pragma: no cover
Preview = MockPreview() # pragma: no cover
class MockSelf:# pragma: no cover
    mode = 'some_mode'# pragma: no cover
    def visit_stmt(self, node, keywords, parens):# pragma: no cover
        return 0# pragma: no cover
    def line(self):# pragma: no cover
        return 1# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 0# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockChild:# pragma: no cover
    def __init__(self, type_: str, children: List = None):# pragma: no cover
        self.type = type_# pragma: no cover
        self.children = children or []# pragma: no cover
# pragma: no cover
node = MockChild('function_def', children=[MockChild('RARROW'), MockChild('atom', [MockChild('LPAR')])]) # pragma: no cover
class MockToken:# pragma: no cover
    RARROW = 'RARROW'# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
# pragma: no cover
token = MockToken() # pragma: no cover
class MockSyms:# pragma: no cover
    atom = 'atom'# pragma: no cover
# pragma: no cover
syms = MockSyms() # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma):# pragma: no cover
    return True# pragma: no cover
 # pragma: no cover
def wrap_in_parentheses(node, child, visible):# pragma: no cover
    pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Visit function definition."""
if Preview.annotation_parens not in self.mode:
    _l_(5720)

    aux = self.visit_stmt(node, keywords={"def"}, parens=set())
    _l_(5706)
    exit(aux)
else:
    aux = self.line()
    _l_(5707)
    exit(aux)

    # Remove redundant brackets around return type annotation.
    is_return_annotation = False
    _l_(5708)
    for child in node.children:
        _l_(5717)

        if child.type == token.RARROW:
            _l_(5716)

            is_return_annotation = True
            _l_(5709)
        elif is_return_annotation:
            _l_(5715)

            if child.type == syms.atom and child.children[0].type == token.LPAR:
                _l_(5713)

                if maybe_make_parens_invisible_in_atom(
                    child,
                    parent=node,
                    remove_brackets_around_comma=False,
                ):
                    _l_(5711)

                    wrap_in_parentheses(node, child, visible=False)
                    _l_(5710)
            else:
                wrap_in_parentheses(node, child, visible=False)
                _l_(5712)
            is_return_annotation = False
            _l_(5714)

    for child in node.children:
        _l_(5719)

        aux = self.visit(child)
        _l_(5718)
        exit(aux)
