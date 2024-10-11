class Parent:# pragma: no cover
    def __init__(self, node_type):# pragma: no cover
        self.type = node_type # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, parent):# pragma: no cover
        self.parent = parent # pragma: no cover
node = Node(Parent('example_type')) # pragma: no cover

class MockParent:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.type = 'exampleType' # pragma: no cover
node = type('MockNode', (object,), {'parent': MockParent()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""
    Returns:
        @node.parent.type, if @node is not None and has a parent.
            OR
        None, otherwise.
    """
if node is None or node.parent is None:
    _l_(3833)

    aux = None
    _l_(3832)
    exit(aux)
aux = node.parent.type
_l_(3834)

exit(aux)
