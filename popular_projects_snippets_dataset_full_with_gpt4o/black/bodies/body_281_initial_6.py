from typing import List, Any # pragma: no cover

class Leaf:# pragma: no cover
    pass # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, prev_sibling=None, parent=None, leaves=None):# pragma: no cover
        self.prev_sibling = prev_sibling# pragma: no cover
        self.parent = parent# pragma: no cover
        self._leaves = leaves or []# pragma: no cover
# pragma: no cover
    def leaves(self) -> List[Any]:# pragma: no cover
        return self._leaves# pragma: no cover
# pragma: no cover
# Example instantiation. You may need to modify it based on your context.# pragma: no cover
node = MockNode(# pragma: no cover
    prev_sibling=MockNode(),# pragma: no cover
    parent=MockNode(# pragma: no cover
        prev_sibling=MockNode(),# pragma: no cover
        parent=None,# pragma: no cover
        leaves=[Leaf()]# pragma: no cover
    )# pragma: no cover
) # pragma: no cover

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
