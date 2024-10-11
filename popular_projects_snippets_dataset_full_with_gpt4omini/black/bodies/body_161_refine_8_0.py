from typing import Any, List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

class MockNode:  # Placeholder for Node class# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [self]  # Simplified for demonstration # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return MockNode(syms.listmaker)  # Simulating an open square bracket # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
def child_towards(node, leaf):  # Mock function for demo# pragma: no cover
    return MockNode('some_type') if leaf else None # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
Node = MockNode # pragma: no cover
syms = MockSyms() # pragma: no cover
leaf = 'example_leaf' # pragma: no cover
TEST_DESCENDANTS = ['some_type', 'other_type'] # pragma: no cover

from typing import List, Optional # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type, next_sibling=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.next_sibling = next_sibling# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [self]  # Simplified for demonstration # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return MockNode(type='open_lsqb', next_sibling=MockNode(type='subscriptlist')) # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
def child_towards(node, leaf):  # Mock function to return a Node# pragma: no cover
    return MockNode(type='subscriptlist') if leaf else None # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
syms = MockSyms() # pragma: no cover
leaf = 'example_leaf' # pragma: no cover
TEST_DESCENDANTS = ['test1', 'test2'] # pragma: no cover

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
