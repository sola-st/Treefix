import sys # pragma: no cover

class MockParent: # pragma: no cover
    def __init__(self, type_value): # pragma: no cover
        self.type = type_value # pragma: no cover
 # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, parent=None): # pragma: no cover
        self.parent = parent # pragma: no cover
 # pragma: no cover
node = MockNode() # pragma: no cover

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
    _l_(15629)

    aux = None
    _l_(15628)
    exit(aux)
aux = node.parent.type
_l_(15630)

exit(aux)
