from typing import Any, List # pragma: no cover
class Node: pass # pragma: no cover
class Mock: pass # pragma: no cover

Node = type('Node', (object,), {'type': None, 'pre_order': lambda self: []}) # pragma: no cover
syms = type('syms', (object,), {'listmaker': 'listmaker', 'subscriptlist': 'subscriptlist'}) # pragma: no cover
def child_towards(subscript_start, leaf): return None # pragma: no cover
leaf = type('MockLeaf', (object,), {})() # pragma: no cover
TEST_DESCENDANTS = {'test1', 'test2'} # pragma: no cover

from typing import Any, List # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.next_sibling = None# pragma: no cover
        self.children = []# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [self] + self.children # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        node = MockNode(type='open_lsqb')# pragma: no cover
        node.next_sibling = MockNode(type='subscriptlist')# pragma: no cover
        return node # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
def child_towards(subscript_start, leaf):# pragma: no cover
    return subscript_start if subscript_start.type == 'test' else None # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
syms = MockSyms() # pragma: no cover
leaf = 'leaf_representation' # pragma: no cover
TEST_DESCENDANTS = {'test1', 'test2'} # pragma: no cover

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
