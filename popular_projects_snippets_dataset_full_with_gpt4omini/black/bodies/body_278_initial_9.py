from typing import Any, Dict, Callable, Optional # pragma: no cover

class MockNode: pass # pragma: no cover
node = MockNode() # pragma: no cover
node.type = 257 # pragma: no cover
class MockToken: pass # pragma: no cover
token = MockToken() # pragma: no cover
token.tok_name = {0: 'ENDMARKER', 1: 'NAME', 2: 'NUMBER', 257: 'NEWTYPE'} # pragma: no cover
def mock_visit_default(self, node): return 'default visited' # pragma: no cover
self = type('MockSelf', (), {'visit_default': mock_visit_default})() # pragma: no cover
def type_repr(value): return f'Type-{value}' # pragma: no cover

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
