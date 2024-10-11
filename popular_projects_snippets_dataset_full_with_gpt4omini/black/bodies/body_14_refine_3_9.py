from enum import Enum # pragma: no cover
from typing import Any, List, Dict, Set # pragma: no cover

class Preview:# pragma: no cover
    annotation_parens = '()' # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = 'default'# pragma: no cover
        self.child = None# pragma: no cover
    def visit_stmt(self, node: Any, keywords: Dict[str, Any], parens: Set[str]) -> Any:# pragma: no cover
        return 'visit_stmt result'# pragma: no cover
    def line(self):# pragma: no cover
        return 'line result'# pragma: no cover
    def visit(self, child: Any) -> Any:# pragma: no cover
        return 'visit result' # pragma: no cover
node = type('Node', (object,), {'children': [], 'type': None})() # pragma: no cover
class Token:# pragma: no cover
    RARROW = '->'# pragma: no cover
    LPAR = '(' # pragma: no cover
class Syms:# pragma: no cover
    atom = 'atom' # pragma: no cover
def maybe_make_parens_invisible_in_atom(child: Any, parent: Any, remove_brackets_around_comma: bool) -> bool:# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node: Any, child: Any, visible: bool) -> None:# pragma: no cover
    pass # pragma: no cover
self = Mock() # pragma: no cover

from typing import Any, List, Dict, Set # pragma: no cover

class Preview:# pragma: no cover
    annotation_parens = '()' # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.mode = 'default'# pragma: no cover
    def visit_stmt(self, node: Any, keywords: Dict[str, Any], parens: Set[str]) -> Any:# pragma: no cover
        return 1  # Ensure it returns a valid callable result# pragma: no cover
    def line(self):# pragma: no cover
        return 'line result'# pragma: no cover
    def visit(self, child: Any) -> Any:# pragma: no cover
        return 'visit result' # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, children: List):# pragma: no cover
        self.children = children# pragma: no cover
class MockChild:# pragma: no cover
    def __init__(self, type: str, children: List = None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children or [] # pragma: no cover
class Token:# pragma: no cover
    RARROW = '->'# pragma: no cover
    LPAR = '(' # pragma: no cover
class Syms:# pragma: no cover
    atom = 'atom' # pragma: no cover
def maybe_make_parens_invisible_in_atom(child: Any, parent: Any, remove_brackets_around_comma: bool) -> bool:# pragma: no cover
    return True # pragma: no cover
def wrap_in_parentheses(node: Any, child: Any, visible: bool) -> None:# pragma: no cover
    pass # pragma: no cover
self = Mock() # pragma: no cover

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
