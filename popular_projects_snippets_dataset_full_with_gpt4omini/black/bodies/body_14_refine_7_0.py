from typing import List, Dict, Any, Callable # pragma: no cover
import token # pragma: no cover

class MockPreview:# pragma: no cover
    annotation_parens = '()'# pragma: no cover
# pragma: no cover
Preview = MockPreview() # pragma: no cover
class MockSelf:# pragma: no cover
    mode = 'some_mode'# pragma: no cover
    def visit_stmt(self, node, keywords, parens):# pragma: no cover
        return 'visit_stmt_result'# pragma: no cover
    def line(self):# pragma: no cover
        return 'line_result'# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'visit_result'# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        pass
# pragma: no cover
node = MockNode() # pragma: no cover
class MockChild:# pragma: no cover
    def __init__(self, child_type):# pragma: no cover
        self.type = child_type# pragma: no cover
        self.children = [MockChild('child_content')] if child_type == syms.atom else [] # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: True # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

from typing import List, Dict, Any, Callable # pragma: no cover

class MockPreview:# pragma: no cover
    annotation_parens = '()'# pragma: no cover
# pragma: no cover
Preview = MockPreview() # pragma: no cover
class MockSelf:# pragma: no cover
    mode = 'some_mode'# pragma: no cover
    def visit_stmt(self, node, keywords, parens):# pragma: no cover
        return 'visit_stmt_result'# pragma: no cover
    def line(self):# pragma: no cover
        return 'line_result'# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'visit_result'# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        pass
# pragma: no cover
node = MockNode() # pragma: no cover
class MockChild:# pragma: no cover
    def __init__(self, child_type):# pragma: no cover
        self.type = child_type# pragma: no cover
        self.children = [] if child_type in ['RARROW', 'atom'] else [MockChild('child_content')] # pragma: no cover
token = type('Token', (object,), {'RARROW': 'RARROW', 'LPAR': 'LPAR'})() # pragma: no cover
syms = type('Syms', (object,), {'atom': 'atom'})() # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: True # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

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
