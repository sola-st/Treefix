from collections import namedtuple # pragma: no cover

Preview = type('Preview', (object,), {'annotation_parens': 'annotation_parens'}) # pragma: no cover
self = type('Mock', (object,), {'mode': 'default', 'visit_stmt': lambda self, node, keywords, parens: 'visit_stmt_result', 'line': lambda self: 'line_result', 'visit': lambda self, child: 'visit_child_result'})() # pragma: no cover
token = namedtuple('Token', ['RARROW', 'LPAR'])(RARROW='RARROW_TYPE', LPAR='LPAR_TYPE') # pragma: no cover
syms = namedtuple('Syms', ['atom'])('ATOM_TYPE') # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: 'make_parens_invisible' # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: 'wrap_in_parentheses_result' # pragma: no cover

from collections import namedtuple # pragma: no cover

Preview = type('Preview', (object,), {'annotation_parens': 'annotation_parens'}) # pragma: no cover
token = type('MockToken', (object,), {'RARROW': 'RARROW_TYPE', 'LPAR': 'LPAR_TYPE'}) # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 'ATOM_TYPE'}) # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: 'make_parens_invisible' # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: 'wrap_in_parentheses_result' # pragma: no cover
node_children = [type('Child', (object,), {'type': token.RARROW, 'children': []})(), type('Child', (object,), {'type': syms.atom, 'children': [type('AtomChild', (object,), {'type': token.LPAR})()]})()] # pragma: no cover
node = type('Node', (object,), {'children': node_children})() # pragma: no cover
self = type('MockSelf', (object,), {'mode': ['default'], 'visit_stmt': lambda self, n, keywords, parens: 'visit_stmt_result', 'line': lambda self: 'line_result', 'visit': lambda self, c: 'visit_child_result'})() # pragma: no cover

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
