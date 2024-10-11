from dataclasses import dataclass, field # pragma: no cover

@dataclass# pragma: no cover
class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return None # pragma: no cover
@dataclass# pragma: no cover
class MockSelf:# pragma: no cover
    bracket_tracker: MockBracketTracker = field(default_factory=MockBracketTracker) # pragma: no cover
@dataclass# pragma: no cover
class Node:# pragma: no cover
    type: int# pragma: no cover
    next_sibling: 'Node' = None# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [] # pragma: no cover
syms = type('syms', (object,), {'listmaker': 1, 'subscriptlist': 2}) # pragma: no cover
def child_towards(subscript_start, leaf):# pragma: no cover
    return subscript_start # pragma: no cover
leaf = Node(type=0) # pragma: no cover
TEST_DESCENDANTS = set([1, 2, 3]) # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return True iff `leaf` is part of a slice with non-trivial exprs."""
open_lsqb = self.bracket_tracker.get_open_lsqb()
_l_(16764)
if open_lsqb is None:
    _l_(16766)

    aux = False
    _l_(16765)
    exit(aux)

subscript_start = open_lsqb.next_sibling
_l_(16767)

if isinstance(subscript_start, Node):
    _l_(16772)

    if subscript_start.type == syms.listmaker:
        _l_(16769)

        aux = False
        _l_(16768)
        exit(aux)

    if subscript_start.type == syms.subscriptlist:
        _l_(16771)

        subscript_start = child_towards(subscript_start, leaf)
        _l_(16770)
aux = subscript_start is not None and any(
    n.type in TEST_DESCENDANTS for n in subscript_start.pre_order()
)
_l_(16773)
exit(aux)
