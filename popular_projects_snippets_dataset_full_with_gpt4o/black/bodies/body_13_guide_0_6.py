import token # pragma: no cover
def maybe_make_parens_invisible_in_atom(child, parent, remove_brackets_around_comma): return True # pragma: no cover
def wrap_in_parentheses(node, child, visible): pass # pragma: no cover

class Node: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.type = None # pragma: no cover
        self.children = [] # pragma: no cover
node = Node() # pragma: no cover
node.children.append(Node()) # pragma: no cover
node.children.append(Node()) # pragma: no cover
node.children[0].type = token.COLON # pragma: no cover
class Mode: # pragma: no cover
    wrap_long_dict_values_in_parens = 'wrap_long_dict_values_in_parens' # pragma: no cover
self = type('Mock', (object,), {'mode': [Mode.wrap_long_dict_values_in_parens]}) # pragma: no cover
class Visitor: # pragma: no cover
    def visit_default(self, node): return 'default' # pragma: no cover
aux = None # pragma: no cover

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
