from typing import List, Optional # pragma: no cover

class Leaf: pass # pragma: no cover

from typing import List, Optional # pragma: no cover

class Leaf:  # Mock Leaf class# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, prev_sibling: Optional['MockNode'] = None, parent: Optional['MockNode'] = None):# pragma: no cover
        self.prev_sibling = prev_sibling# pragma: no cover
        self.parent = parent# pragma: no cover
# pragma: no cover
    def leaves(self) -> List[Leaf]:# pragma: no cover
        return []  # Mock leaves method returning an empty list# pragma: no cover
# pragma: no cover
# Create a mock leaf and parent nodes# pragma: no cover
leaf = Leaf()  # Create a leaf instance# pragma: no cover
parent = MockNode()  # Create a parent node# pragma: no cover
sibling = MockNode(leaf, parent)  # Create a sibling node pointing to the leaf# pragma: no cover
node = sibling  # Initialize the node to point to the sibling # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return the first leaf that precedes `node`, if any."""
while node:
    _l_(4870)

    res = node.prev_sibling
    _l_(4861)
    if res:
        _l_(4868)

        if isinstance(res, Leaf):
            _l_(4863)

            aux = res
            _l_(4862)
            exit(aux)

        try:
            _l_(4867)

            aux = list(res.leaves())[-1]
            _l_(4864)
            exit(aux)

        except IndexError:
            _l_(4866)

            aux = None
            _l_(4865)
            exit(aux)

    node = node.parent
    _l_(4869)
aux = None
_l_(4871)
exit(aux)
