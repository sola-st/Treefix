from typing import Any, List # pragma: no cover
import sys # pragma: no cover
from types import SimpleNamespace # pragma: no cover

node = SimpleNamespace(type='atom', children=[SimpleNamespace(type='LPAR'), SimpleNamespace(type='child1'), SimpleNamespace(type='RPAR')]) # pragma: no cover
syms = SimpleNamespace(atom='atom') # pragma: no cover
token = SimpleNamespace(LPAR='LPAR', RPAR='RPAR') # pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'mark': lambda self, l: None, 'max_delimiter_priority': lambda self: 5}) # pragma: no cover
Leaf = type('Leaf', (object,), {}) # pragma: no cover

from typing import Any, List # pragma: no cover
import sys # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type_: str):# pragma: no cover
        self.type = type_# pragma: no cover
# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'MockLeaf(type={self.type})'# pragma: no cover
# pragma: no cover
class MockNodeChild:# pragma: no cover
    def __init__(self, type_: str, leaves: List[MockLeaf] = None):# pragma: no cover
        self.type = type_# pragma: no cover
        self._leaves = leaves or []# pragma: no cover
# pragma: no cover
    def leaves(self):# pragma: no cover
        return self._leaves# pragma: no cover
# pragma: no cover
node = SimpleNamespace(# pragma: no cover
    type='atom',# pragma: no cover
    children=[# pragma: no cover
        MockLeaf('LPAR'),# pragma: no cover
        MockNodeChild('content', leaves=[MockLeaf('child1'), MockLeaf('child2')]),# pragma: no cover
        MockLeaf('RPAR')# pragma: no cover
    ]# pragma: no cover
)# pragma: no cover
syms = SimpleNamespace(atom='atom')# pragma: no cover
token = SimpleNamespace(LPAR='LPAR', RPAR='RPAR')# pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'mark': lambda self, l: None, 'max_delimiter_priority': lambda self: 5})# pragma: no cover
Leaf = MockLeaf # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""Return maximum delimiter priority inside `node`.

    This is specific to atoms with contents contained in a pair of parentheses.
    If `node` isn't an atom or there are no enclosing parentheses, returns 0.
    """
if node.type != syms.atom:
    _l_(19507)

    aux = 0
    _l_(19506)
    exit(aux)

first = node.children[0]
_l_(19508)
last = node.children[-1]
_l_(19509)
if not (first.type == token.LPAR and last.type == token.RPAR):
    _l_(19511)

    aux = 0
    _l_(19510)
    exit(aux)

bt = BracketTracker()
_l_(19512)
for c in node.children[1:-1]:
    _l_(19517)

    if isinstance(c, Leaf):
        _l_(19516)

        bt.mark(c)
        _l_(19513)
    else:
        for leaf in c.leaves():
            _l_(19515)

            bt.mark(leaf)
            _l_(19514)
try:
    _l_(19521)

    aux = bt.max_delimiter_priority()
    _l_(19518)
    exit(aux)

except ValueError:
    _l_(19520)

    aux = 0
    _l_(19519)
    exit(aux)
