from typing import List, Any, Union # pragma: no cover

leaf = type('MockLeaf', (object,), {})() # pragma: no cover
TEST_DESCENDANTS = {1, 2, 3} # pragma: no cover
Node = type('MockNode', (object,), {'pre_order': lambda self: [type('MockNodeChild', (object,), {'type': 1})()] }) # pragma: no cover
syms = type('MockSyms', (object,), {'listmaker': 1, 'subscriptlist': 2}) # pragma: no cover
child_towards = lambda subscript_start, leaf: Node() # pragma: no cover
bracket_tracker = type('MockBracketTracker', (object,), {'get_open_lsqb': lambda: type('MockLSQB', (object,), {'next_sibling': Node()})()}) # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': bracket_tracker})() # pragma: no cover

from typing import List, Any, Union # pragma: no cover

leaf = type('MockLeaf', (object,), {})() # pragma: no cover
TEST_DESCENDANTS = {1, 2, 3} # pragma: no cover
Node = type('MockNode', (object,), {'pre_order': lambda self: [type('MockNodeChild', (object,), {'type': 1})()], 'type': None}) # pragma: no cover
syms = type('MockSyms', (object,), {'listmaker': 1, 'subscriptlist': 2}) # pragma: no cover
child_towards = lambda subscript_start, leaf: Node() # pragma: no cover
bracket_tracker = type('MockBracketTracker', (object,), {'get_open_lsqb': lambda: type('MockLSQB', (object,), {'next_sibling': type('MockNode', (object,), {'type': 0})()})()}) # pragma: no cover
self = type('MockSelf', (object,), {'bracket_tracker': bracket_tracker})() # pragma: no cover

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
