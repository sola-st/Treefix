node = type('Mock', (object,), {'children': [type('MockChild', (object,), {})()]})() # pragma: no cover
Node = node.__class__ # pragma: no cover
self = type('Mock', (object,), {'visit': lambda self, x: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Default `visit_*()` implementation. Recurses to children of `node`."""
if isinstance(node, Node):
    _l_(18069)

    for child in node.children:
        _l_(18068)

        aux = self.visit(child)
        _l_(18067)
        exit(aux)
