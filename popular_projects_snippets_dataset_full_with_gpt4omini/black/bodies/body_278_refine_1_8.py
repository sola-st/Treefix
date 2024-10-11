import types # pragma: no cover
from types import SimpleNamespace # pragma: no cover

node = SimpleNamespace(type=42) # pragma: no cover
token = SimpleNamespace(tok_name={42: 'simple_stmt'}) # pragma: no cover
type_repr = lambda x: f'Type({x})' # pragma: no cover
self = type('Mock', (), {'visit_default': lambda x: 'default_visit'})() # pragma: no cover

import types # pragma: no cover
from types import SimpleNamespace # pragma: no cover

node = SimpleNamespace(type=42) # pragma: no cover
token = SimpleNamespace(tok_name={42: 'simple_stmt'}) # pragma: no cover
type_repr = lambda x: f'Type({x})' # pragma: no cover
class MockSelf:# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'Visited default node'# pragma: no cover
self = MockSelf() # pragma: no cover

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
    _l_(4629)

    name = token.tok_name[node.type]
    _l_(4627)
else:
    name = str(type_repr(node.type))
    _l_(4628)
# We explicitly branch on whether a visitor exists (instead of
# using self.visit_default as the default arg to getattr) in order
# to save needing to create a bound method object and so mypyc can
# generate a native call to visit_default.
visitf = getattr(self, f"visit_{name}", None)
_l_(4630)
if visitf:
    _l_(4633)

    aux = visitf(node)
    _l_(4631)
    exit(aux)
else:
    aux = self.visit_default(node)
    _l_(4632)
    exit(aux)
