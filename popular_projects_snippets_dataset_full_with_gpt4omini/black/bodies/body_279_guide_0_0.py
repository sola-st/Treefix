class Node: # pragma: no cover
    def __init__(self, children=[]): # pragma: no cover
        self.children = children # pragma: no cover
class Visitor: # pragma: no cover
    def visit(self, node): # pragma: no cover
        pass  # This is a placeholder for the actual implementation # pragma: no cover

child1 = Node() # pragma: no cover
child2 = Node() # pragma: no cover
node = Node(children=[child1, child2]) # pragma: no cover
self = Visitor() # pragma: no cover

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
