from types import SimpleNamespace # pragma: no cover
import token # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.mode = [getattr('Preview', 'wrap_long_dict_values_in_parens', 'Preview.wrap_long_dict_values_in_parens')] # pragma: no cover
node = SimpleNamespace(children=[SimpleNamespace(type=token.COLON, children=[SimpleNamespace(type=token.LPAR)]), SimpleNamespace(type=token.NAME)]) # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma): return False # pragma: no cover
def wrap_in_parentheses(node, child, visible): pass # pragma: no cover
def some_undefined_method(node): return 'aux_value' # pragma: no cover
self.visit_default = some_undefined_method # pragma: no cover

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
