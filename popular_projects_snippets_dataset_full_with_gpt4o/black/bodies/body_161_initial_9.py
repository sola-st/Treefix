from typing import List # pragma: no cover
from typing import Any # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def get_open_lsqb(self): # pragma: no cover
        # A mock method to return an object with a 'next_sibling' attribute # pragma: no cover
        class MockNode: # pragma: no cover
            next_sibling = self # pragma: no cover
        return MockNode() # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    bracket_tracker = MockBracketTracker() # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
 # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, node_type: Any): # pragma: no cover
        self.type = node_type # pragma: no cover
    def pre_order(self) -> List: # pragma: no cover
        return [self] # pragma: no cover
 # pragma: no cover
class symsPlaceholder: # pragma: no cover
    listmaker = 1 # pragma: no cover
    subscriptlist = 2 # pragma: no cover
 # pragma: no cover
syms = symsPlaceholder() # pragma: no cover
 # pragma: no cover
def child_towards(node: Node, leaf: Node) -> Node: # pragma: no cover
    # Mock function to return a Node instance # pragma: no cover
    return node # pragma: no cover
 # pragma: no cover
leaf = Node(3) # pragma: no cover
 # pragma: no cover
TEST_DESCENDANTS = set([1, 2, 3]) # pragma: no cover

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
