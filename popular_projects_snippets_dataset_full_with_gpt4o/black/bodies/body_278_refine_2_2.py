import token # pragma: no cover

node = type('MockNode', (object,), {'type': 255})() # pragma: no cover
token.tok_name = {i: 'TOKEN_NAME_' + str(i) for i in range(256)} # pragma: no cover
type_repr = lambda x: 'TYPE_REPR_' + str(x) # pragma: no cover
self = type('MockVisitor', (object,), {'visit_default': lambda self, node: 'DEFAULT_VISIT'}) # pragma: no cover

import token # pragma: no cover

node = type('MockNode', (object,), {'type': 255})() # pragma: no cover
token.tok_name = {i: 'TOKEN_NAME_' + str(i) for i in range(256)} # pragma: no cover
type_repr = lambda x: 'TYPE_REPR_' + str(x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Main method to visit `node` and its children.

        It tries to find a `visit_*()` method for the given `node.type`, like
        `visit_simple_stmt` for Node objects or `visit_INDENT` for Leaf objects.
        If no dedicated `visit_*()` method is found, chooses `visit_default()`
        instead.

        Then yields objects of type `T` from the selected visitor.
        """
if node.type < 256:
    _l_(16264)

    name = token.tok_name[node.type]
    _l_(16262)
else:
    name = str(type_repr(node.type))
    _l_(16263)
# We explicitly branch on whether a visitor exists (instead of
# using self.visit_default as the default arg to getattr) in order
# to save needing to create a bound method object and so mypyc can
# generate a native call to visit_default.
visitf = getattr(self, f"visit_{name}", None)
_l_(16265)
if visitf:
    _l_(16268)

    aux = visitf(node)
    _l_(16266)
    exit(aux)
else:
    aux = self.visit_default(node)
    _l_(16267)
    exit(aux)
