# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Default `visit_*()` implementation. Recurses to children of `node`."""
if isinstance(node, Node):
    _l_(6290)

    for child in node.children:
        _l_(6289)

        aux = self.visit(child)
        _l_(6288)
        exit(aux)
