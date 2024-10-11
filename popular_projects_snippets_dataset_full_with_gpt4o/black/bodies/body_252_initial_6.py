from typing import List, Union # pragma: no cover
from enum import Enum, auto # pragma: no cover

class NodeType(Enum): atom = auto() # pragma: no cover
class TokenType(Enum): LPAR = auto(); RPAR = auto() # pragma: no cover
class MockLeaf: pass # pragma: no cover
class MockNodeType: type = NodeType.atom; children: List[Union['MockLeaf', 'MockNodeType']] = [MockLeaf(), MockLeaf(), MockLeaf()] # pragma: no cover
node = MockNodeType() # pragma: no cover
syms = type('Mock', (object,), {'atom': NodeType.atom}) # pragma: no cover
token = type('Mock', (object,), {'LPAR': TokenType.LPAR, 'RPAR': TokenType.RPAR}) # pragma: no cover

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
