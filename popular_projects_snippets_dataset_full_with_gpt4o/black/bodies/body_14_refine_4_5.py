from types import SimpleNamespace # pragma: no cover
from typing import Any, Dict # pragma: no cover

Preview = type('Mock', (object,), {'annotation_parens': {'@'}})() # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'mode': set(),# pragma: no cover
    'visit_stmt': lambda self, node, keywords, parens: 'visit_stmt called',# pragma: no cover
    'line': lambda self: 'line called',# pragma: no cover
    'visit': lambda self, child: 'visit called'# pragma: no cover
})() # pragma: no cover
node = type('Mock', (object,), {'children': []}) # pragma: no cover
token = SimpleNamespace(RARROW=1, LPAR=2) # pragma: no cover
syms = SimpleNamespace(atom=3) # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: False # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

from types import SimpleNamespace # pragma: no cover
from typing import Any, Dict # pragma: no cover

Preview = type('Mock', (object,), {'annotation_parens': {'@'}})() # pragma: no cover
node = SimpleNamespace(children=[SimpleNamespace(type=1, children=[]), SimpleNamespace(type=3, children=[SimpleNamespace(type=2)])]) # pragma: no cover
token = SimpleNamespace(RARROW=1, LPAR=2) # pragma: no cover
syms = SimpleNamespace(atom=3) # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: False # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'mode': set(),# pragma: no cover
    'visit_stmt': lambda self, node, keywords, parens: None,# pragma: no cover
    'line': lambda self: None,# pragma: no cover
    'visit': lambda self, child: None# pragma: no cover
})() # pragma: no cover

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
