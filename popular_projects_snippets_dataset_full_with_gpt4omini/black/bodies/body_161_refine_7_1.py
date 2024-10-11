from typing import List, Optional # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type# pragma: no cover
# pragma: no cover
class BracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return Node('lsqb')# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    bracket_tracker = BracketTracker()# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
syms = type('MockSyms', (), {'listmaker': 'listmaker_type', 'subscriptlist': 'subscriptlist_type'}) # pragma: no cover
leaf = 'leaf_example' # pragma: no cover
TEST_DESCENDANTS = ['test_descendant_1', 'test_descendant_2'] # pragma: no cover
def child_towards(start_node, leaf_node):# pragma: no cover
    return Node('subscriptlist') if start_node.type == 'lsqb' else None # pragma: no cover

from typing import List # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type, next_sibling=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.next_sibling = next_sibling# pragma: no cover
        self.children = []# pragma: no cover
    def add_child(self, child):# pragma: no cover
        self.children.append(child)# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [self] + [child for child in self.children for child in child.pre_order()] # pragma: no cover
class BracketTracker:# pragma: no cover
    def get_open_lsqb(self):# pragma: no cover
        return Node('open_lsqb', Node('subscriptlist')) # pragma: no cover
class Mock:# pragma: no cover
    bracket_tracker = BracketTracker()# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
syms = type('MockSyms', (), {'listmaker': 'listmaker_type', 'subscriptlist': 'subscriptlist_type'}) # pragma: no cover
leaf = 'leaf_example' # pragma: no cover
TEST_DESCENDANTS = {'test_type1', 'test_type2'} # pragma: no cover
def child_towards(node, leaf): return Node('subscriptlist') if node.type == 'open_lsqb' else None # pragma: no cover

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
