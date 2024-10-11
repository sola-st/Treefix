from typing import Any, List # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return MockNode(type='open_lsqb') # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, type=None, children=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children or []# pragma: no cover
    def pre_order(self):# pragma: no cover
        return self.children # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
def child_towards(node, leaf):# pragma: no cover
    return node.children[0] if node.children else None # pragma: no cover
leaf = 'leaf_value' # pragma: no cover
TEST_DESCENDANTS = ['descendant1', 'descendant2'] # pragma: no cover
self = type('Mock', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
syms = MockSyms() # pragma: no cover

from typing import Any, List # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return MockNode(type='open_lsqb', next_sibling=self.create_subscript_list())# pragma: no cover
    def create_subscript_list(self):# pragma: no cover
        return MockNode(type='subscriptlist', children=[MockNode(type='test1'), MockNode(type='test2')]) # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, type=None, children=None, next_sibling=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children or []# pragma: no cover
        self.next_sibling = next_sibling# pragma: no cover
    def pre_order(self):# pragma: no cover
        return self.children # pragma: no cover
class MockSyms:# pragma: no cover
    listmaker = 'listmaker'# pragma: no cover
    subscriptlist = 'subscriptlist' # pragma: no cover
def child_towards(node, leaf):# pragma: no cover
    for child in node.children:# pragma: no cover
        if child.type == leaf:# pragma: no cover
            return child# pragma: no cover
    return None # pragma: no cover
leaf = 'test1' # pragma: no cover
TEST_DESCENDANTS = ['test1', 'test2'] # pragma: no cover
self = type('Mock', (object,), {'bracket_tracker': MockBracketTracker()})() # pragma: no cover
syms = MockSyms() # pragma: no cover

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
