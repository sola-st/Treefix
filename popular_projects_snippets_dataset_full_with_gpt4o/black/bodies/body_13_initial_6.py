from types import SimpleNamespace # pragma: no cover
import token # pragma: no cover
import ast # pragma: no cover

Preview = SimpleNamespace(wrap_long_dict_values_in_parens=True) # pragma: no cover
self = SimpleNamespace(mode=[True], visit_default=lambda node: None) # pragma: no cover
node = SimpleNamespace(children=[SimpleNamespace(type=token.COLON), SimpleNamespace(type=token.LPAR), SimpleNamespace(type=0)]) # pragma: no cover
token = SimpleNamespace(COLON=token.COLON, LPAR=token.LPAR) # pragma: no cover
syms = SimpleNamespace(atom=ast.Expr) # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: False # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None # pragma: no cover

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
