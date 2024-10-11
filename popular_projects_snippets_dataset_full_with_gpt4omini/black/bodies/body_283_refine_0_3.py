class MockParent:  # Create a mock class for the parent# pragma: no cover
    def __init__(self, type_):# pragma: no cover
        self.type = type_# pragma: no cover
# pragma: no cover
node = type('Mock', (object,), {'parent': MockParent('exampleType')})()  # Initialize node with a parent that has a type # pragma: no cover

class MockParent:  # Create a mock class for the parent# pragma: no cover
    def __init__(self, type_):# pragma: no cover
        self.type = type_# pragma: no cover
# pragma: no cover
node = type('Mock', (object,), {'parent': MockParent('exampleType')})()  # Initialize node with a parent that has a type # pragma: no cover

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
