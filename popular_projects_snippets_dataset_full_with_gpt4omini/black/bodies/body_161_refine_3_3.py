from typing import List, Optional # pragma: no cover

class MockNode: pass # pragma: no cover
class MockSyms: pass # pragma: no cover
syms = MockSyms() # pragma: no cover
syms.listmaker = 'listmaker' # pragma: no cover
syms.subscriptlist = 'subscriptlist' # pragma: no cover
class MockBracketTracker: pass # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.bracket_tracker = MockBracketTracker() # pragma: no cover
self.bracket_tracker.get_open_lsqb = lambda: MockNode() # pragma: no cover
leaf = 'leaf_representation' # pragma: no cover
TEST_DESCENDANTS = {'test1', 'test2'} # pragma: no cover
MockNode.type = 'mock_node_type' # pragma: no cover
Node = MockNode # pragma: no cover
MockNode.pre_order = lambda: [MockNode(type='test1'), MockNode(type='test2')] # pragma: no cover
def child_towards(node, leaf): return node if node.type == 'test' else None # pragma: no cover

from typing import List, Optional # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type=None, next_sibling=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.next_sibling = next_sibling# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [] # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
syms = MockSyms() # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return MockNode(type='open_lsqb', next_sibling=MockNode(type='subscriptlist_node')) # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
leaf = 'leaf_representation' # pragma: no cover
TEST_DESCENDANTS = {'test1', 'test2'} # pragma: no cover
node1 = MockNode(type='test1') # pragma: no cover
node2 = MockNode(type='test2') # pragma: no cover
node1.next_sibling = node2 # pragma: no cover
MockNode.pre_order = lambda self: [node1, node2] # pragma: no cover
def child_towards(node, leaf): return node if node.type == 'test1' else None # pragma: no cover

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
