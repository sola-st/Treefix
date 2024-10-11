from typing import Any, List # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.bracket_tracker = Mock() # pragma: no cover
self.bracket_tracker.get_open_lsqb = lambda: Mock() # pragma: no cover
Node = Mock() # pragma: no cover
Node.type = 'mock_type' # pragma: no cover
syms = Mock() # pragma: no cover
syms.listmaker = 'listmaker_type' # pragma: no cover
syms.subscriptlist = 'subscriptlist_type' # pragma: no cover
def child_towards(node, leaf): return Mock() # pragma: no cover
leaf = 'mock_leaf' # pragma: no cover
TEST_DESCENDANTS = {'test_type'} # pragma: no cover

from typing import List, Optional # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type, next_sibling=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.next_sibling = next_sibling# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [self] # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return MockNode('lsqb', next_sibling=MockNode('subscriptlist')) # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
def child_towards(start_node, leaf):# pragma: no cover
    return MockNode('subscriptlist') if start_node.type == 'lsqb' else None # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
syms = MockSyms() # pragma: no cover
leaf = 'leaf_value' # pragma: no cover
TEST_DESCENDANTS = {'test_type1', 'test_type2'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return True iff `leaf` is part of a slice with non-trivial exprs."""
open_lsqb = self.bracket_tracker.get_open_lsqb()
_l_(5165)
if open_lsqb is None:
    _l_(5167)

    aux = False
    _l_(5166)
    exit(aux)

subscript_start = open_lsqb.next_sibling
_l_(5168)

if isinstance(subscript_start, Node):
    _l_(5173)

    if subscript_start.type == syms.listmaker:
        _l_(5170)

        aux = False
        _l_(5169)
        exit(aux)

    if subscript_start.type == syms.subscriptlist:
        _l_(5172)

        subscript_start = child_towards(subscript_start, leaf)
        _l_(5171)
aux = subscript_start is not None and any(
    n.type in TEST_DESCENDANTS for n in subscript_start.pre_order()
)
_l_(5174)
exit(aux)
