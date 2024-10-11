class MockParent:# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type# pragma: no cover
# pragma: no cover
node = type('Mock', (object,), {'parent': MockParent('example_type')})() # pragma: no cover

class MockParent:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.type = 'example_type'# pragma: no cover
# pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, parent):# pragma: no cover
        self.parent = parent# pragma: no cover
# pragma: no cover
parent_instance = MockParent()# pragma: no cover
node = MockNode(parent_instance) # pragma: no cover

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
