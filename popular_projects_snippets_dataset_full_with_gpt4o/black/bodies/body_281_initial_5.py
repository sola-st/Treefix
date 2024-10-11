from typing import Optional, List # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, value: str): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, value: str, leaves: Optional[List['Node']] = None, parent: Optional['Node'] = None): # pragma: no cover
        self.value = value # pragma: no cover
        self._leaves = leaves or [] # pragma: no cover
        self.parent = parent # pragma: no cover
        self._prev_sibling = None # pragma: no cover
        if parent: # pragma: no cover
            index = parent._leaves.index(self) # pragma: no cover
            if index > 0: # pragma: no cover
                self._prev_sibling = parent._leaves[index - 1] # pragma: no cover
 # pragma: no cover
    @property # pragma: no cover
    def prev_sibling(self): # pragma: no cover
        return self._prev_sibling # pragma: no cover
 # pragma: no cover
    def leaves(self): # pragma: no cover
        return self._leaves # pragma: no cover
 # pragma: no cover
leaf_1 = Leaf('Leaf 1') # pragma: no cover
leaf_2 = Leaf('Leaf 2') # pragma: no cover
 # pragma: no cover
node_2 = Node('Node 2', parent=None) # pragma: no cover
node_1 = Node('Node 1', leaves=[node_2], parent=None) # pragma: no cover
node_2.parent = node_1 # pragma: no cover
 # pragma: no cover
node = node_2 # pragma: no cover

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
