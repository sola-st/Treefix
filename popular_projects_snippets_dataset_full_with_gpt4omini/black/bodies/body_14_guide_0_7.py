import token # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.mode = 'other_mode' # pragma: no cover
self.visit_stmt = lambda node, keywords, parens: 'stmt_visited' # pragma: no cover
self.line = lambda: 'line_visited' # pragma: no cover
self.visit = lambda child: 'child_visited' # pragma: no cover
class Node: pass # pragma: no cover
node = Node() # pragma: no cover
node.children = [Mock()] * 5 # pragma: no cover
node.children[0].type = token.RARROW # pragma: no cover
node.children[1].children = [Mock()] # pragma: no cover
node.children[1].children[0].type = token.LPAR # pragma: no cover
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
