from typing import List, Any # pragma: no cover

class MockNode: pass # pragma: no cover
class MockSyms: pass # pragma: no cover
syms = MockSyms() # pragma: no cover
syms.listmaker = 'listmaker' # pragma: no cover
syms.subscriptlist = 'subscriptlist' # pragma: no cover
node1 = MockNode() # pragma: no cover
node1.type = syms.listmaker # pragma: no cover
node2 = MockNode() # pragma: no cover
node2.type = syms.subscriptlist # pragma: no cover
leaf = 'leaf' # pragma: no cover
TEST_DESCENDANTS = {'test1', 'test2'} # pragma: no cover
class MockBracketTracker: pass # pragma: no cover
mock_bracket_tracker = MockBracketTracker() # pragma: no cover
mock_bracket_tracker.get_open_lsqb = lambda: node1 # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': mock_bracket_tracker})() # pragma: no cover
def child_towards(start, leaf): return node2 # pragma: no cover

from typing import List, Any # pragma: no cover

class MockNode:  # pragma: no cover
    def __init__(self, type_name): # pragma: no cover
        self.type = type_name # pragma: no cover
        self.next_sibling = None # pragma: no cover
        self.children = [] # pragma: no cover
    def add_child(self, child): # pragma: no cover
        self.children.append(child) # pragma: no cover
    def pre_order(self): # pragma: no cover
        yield self # pragma: no cover
        for child in self.children: # pragma: no cover
            yield from child.pre_order() # pragma: no cover
class MockSyms: pass # pragma: no cover
syms = MockSyms() # pragma: no cover
syms.listmaker = 'listmaker' # pragma: no cover
syms.subscriptlist = 'subscriptlist' # pragma: no cover
node1 = MockNode(syms.listmaker) # pragma: no cover
node2 = MockNode(syms.subscriptlist) # pragma: no cover
node1.next_sibling = node2 # pragma: no cover
leaf = 'leaf' # pragma: no cover
TEST_DESCENDANTS = {'test1', 'test2'} # pragma: no cover
class MockBracketTracker: pass # pragma: no cover
mock_bracket_tracker = MockBracketTracker() # pragma: no cover
mock_bracket_tracker.get_open_lsqb = lambda: node1 # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': mock_bracket_tracker})() # pragma: no cover
def child_towards(start, leaf): return node2 # pragma: no cover

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
