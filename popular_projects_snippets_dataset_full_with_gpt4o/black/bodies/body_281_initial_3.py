from typing import List, Optional # pragma: no cover

class Leaf: pass # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, prev_sibling: Optional['MockNode'], parent: Optional['MockNode'], is_leaf: bool = False, leaves: Optional[List['Leaf']] = None): # pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
        self.parent = parent # pragma: no cover
        self.is_leaf = is_leaf # pragma: no cover
        self._leaves = leaves or [] # pragma: no cover
 # pragma: no cover
    def leaves(self): # pragma: no cover
        if self.is_leaf: # pragma: no cover
            return [Leaf()] # pragma: no cover
        return self._leaves # pragma: no cover
 # pragma: no cover
# Creating a mock structure for the nodes # pragma: no cover
leaf_node = MockNode(None, None, is_leaf=True) # pragma: no cover
intermediate_node = MockNode(leaf_node, None) # pragma: no cover
node = MockNode(intermediate_node, None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return the first leaf that precedes `node`, if any."""
while node:
    _l_(16657)

    res = node.prev_sibling
    _l_(16648)
    if res:
        _l_(16655)

        if isinstance(res, Leaf):
            _l_(16650)

            aux = res
            _l_(16649)
            exit(aux)

        try:
            _l_(16654)

            aux = list(res.leaves())[-1]
            _l_(16651)
            exit(aux)

        except IndexError:
            _l_(16653)

            aux = None
            _l_(16652)
            exit(aux)

    node = node.parent
    _l_(16656)
aux = None
_l_(16658)
exit(aux)
