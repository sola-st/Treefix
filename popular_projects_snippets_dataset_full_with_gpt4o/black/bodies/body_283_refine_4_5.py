node = type('MockNode', (object,), {'parent': type('MockParent', (object,), {'type': 'parent_type'})()})() # pragma: no cover

class ParentMock: type = 'parent_type' # pragma: no cover
node = type('MockNode', (object,), {'parent': ParentMock()})() # pragma: no cover

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
