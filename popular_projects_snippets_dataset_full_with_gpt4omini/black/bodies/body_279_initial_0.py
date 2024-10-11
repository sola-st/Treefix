from typing import List # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, children: List['Node']):# pragma: no cover
        self.children = children # pragma: no cover
node = Node(children=[]) # pragma: no cover
class Mock:# pragma: no cover
    def visit(self, child):# pragma: no cover
        return 'Visited'  # Placeholder return value for visit method# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover

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
