from collections import namedtuple # pragma: no cover
import types # pragma: no cover

leaf = namedtuple('Leaf', '')() # pragma: no cover
Node = namedtuple('Node', ['type', 'next_sibling', 'pre_order', 'children']) # pragma: no cover
syms = types.SimpleNamespace(listmaker='listmaker', subscriptlist='subscriptlist') # pragma: no cover
def child_towards(subscript_start, leaf): return Node(type='subtype', next_sibling=None, pre_order=lambda: [Node(type='test', next_sibling=None, pre_order=lambda: [])], children=[]) # pragma: no cover
TEST_DESCENDANTS = {'test'} # pragma: no cover
BracketTracker = namedtuple('BracketTracker', ['get_open_lsqb']) # pragma: no cover
self = type('Mock', (object,), {'bracket_tracker': BracketTracker(get_open_lsqb=lambda: Node(type='subscriptlist', next_sibling=Node(type='test', next_sibling=None, pre_order=lambda: [])))})() # pragma: no cover

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
