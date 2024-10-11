import enum # pragma: no cover

Preview = type('Mock', (object,), {'wrap_long_dict_values_in_parens': 'wrap'}); # pragma: no cover
self = type('Mock', (object,), {'mode': ['wrap'], 'visit_default': lambda self, node: None})(); # pragma: no cover
node = type('Mock', (object,), {'children': [type('Mock', (object,), {'type': 'COLON'})()]})(); # pragma: no cover
token = type('Mock', (object,), {'COLON': 'COLON', 'LPAR': 'LPAR'})(); # pragma: no cover
syms = type('Mock', (object,), {'atom': 'atom'})(); # pragma: no cover
maybe_make_parens_invisible_in_atom = lambda child, parent, remove_brackets_around_comma: True; # pragma: no cover
wrap_in_parentheses = lambda node, child, visible: None; # pragma: no cover

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
