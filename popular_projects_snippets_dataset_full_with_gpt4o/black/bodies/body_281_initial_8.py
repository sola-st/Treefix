from typing import Optional, Union, List # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self, prev_sibling: Optional['MockNode'], parent: Optional['MockNode']): # pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
        self.parent = parent # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class ResMock: # pragma: no cover
    def __init__(self, leaves: List[Leaf]): # pragma: no cover
        self._leaves = leaves # pragma: no cover
 # pragma: no cover
    def leaves(self) -> List[Leaf]: # pragma: no cover
        return self._leaves or [] # pragma: no cover
 # pragma: no cover
leaf1 = Leaf() # pragma: no cover
leaf2 = Leaf() # pragma: no cover
leaf3 = Leaf() # pragma: no cover
 # pragma: no cover
# Creating a hierarchy of nodes and leaves for testing # pragma: no cover
node3 = MockNode(prev_sibling=None, parent=None) # pragma: no cover
node2 = MockNode(prev_sibling=node3, parent=None) # pragma: no cover
node1 = MockNode(prev_sibling=node2, parent=None) # pragma: no cover
 # pragma: no cover
res_with_leaves = ResMock(leaves=[leaf1, leaf2, leaf3]) # pragma: no cover
res_empty = ResMock(leaves=[]) # pragma: no cover
 # pragma: no cover
# Assigning prev_sibling to either a Leaf or ResMock # pragma: no cover
node3.prev_sibling = res_with_leaves # pragma: no cover
node2.prev_sibling = leaf1 # pragma: no cover
node1.prev_sibling = res_empty # pragma: no cover
 # pragma: no cover
node = node1 # pragma: no cover

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
