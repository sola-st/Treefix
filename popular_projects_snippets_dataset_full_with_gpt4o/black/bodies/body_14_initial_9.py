from typing import Any, Set, Dict, List # pragma: no cover

class Preview:# pragma: no cover
    annotation_parens: Set[str] = {"some_parens"} # pragma: no cover
self = type("MockSelf", (object,), {# pragma: no cover
    "mode": {"some_mode"},# pragma: no cover
    "visit_stmt": lambda self, node, keywords, parens: None,# pragma: no cover
    "line": lambda self: None,# pragma: no cover
    "visit": lambda self, child: None# pragma: no cover
})() # pragma: no cover
node = type("MockNode", (object,), {# pragma: no cover
    "children": []# pragma: no cover
})() # pragma: no cover
token = type("MockToken", (object,), {# pragma: no cover
    "RARROW": "rarrow",# pragma: no cover
    "LPAR": "lpar"# pragma: no cover
}) # pragma: no cover
syms = type("MockSyms", (object,), {# pragma: no cover
    "atom": "atom"# pragma: no cover
}) # pragma: no cover
def maybe_make_parens_invisible_in_atom(child: Any, parent: Any, remove_brackets_around_comma: bool) -> bool:# pragma: no cover
    return False # pragma: no cover
def wrap_in_parentheses(node: Any, child: Any, visible: bool) -> None:# pragma: no cover
    pass # pragma: no cover

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
