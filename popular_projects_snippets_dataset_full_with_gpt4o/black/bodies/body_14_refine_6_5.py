import typing # pragma: no cover
from typing import Any # pragma: no cover

Preview = type('MockPreview', (object,), {'annotation_parens': set()}) # pragma: no cover
self = type('MockSelf', (object,), {'mode': set(), 'visit_stmt': lambda self, node, keywords, parens: None, 'line': lambda self: None, 'visit': lambda self, child: None}) # pragma: no cover
node = type('MockNode', (object,), {'children': []}) # pragma: no cover
token = type('MockToken', (object,), {'RARROW': 1, 'LPAR': 2}) # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 3}) # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: True # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

import types # pragma: no cover
from typing import Any # pragma: no cover

Preview = type('MockPreview', (object,), {'annotation_parens': set()}) # pragma: no cover
self = type('MockSelf', (object,), {'mode': set(), 'visit_stmt': lambda node, keywords, parens: None, 'line': lambda: None, 'visit': lambda child: None})() # pragma: no cover
node = types.SimpleNamespace(children=[]) # pragma: no cover
token = types.SimpleNamespace(RARROW=1, LPAR=2) # pragma: no cover
syms = types.SimpleNamespace(atom=3) # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: False # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

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
