from typing import List, Union # pragma: no cover
import token # pragma: no cover

class NodeType: pass # pragma: no cover
 # pragma: no cover
class Syms: # pragma: no cover
    atom = NodeType() # pragma: no cover
 # pragma: no cover
class Token: # pragma: no cover
    LPAR = token.LPAR # pragma: no cover
    RPAR = token.RPAR # pragma: no cover
 # pragma: no cover
class BracketTracker: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.priority = 0 # pragma: no cover
    def mark(self, leaf): # pragma: no cover
        pass  # Assume some logic that modifies self.priority # pragma: no cover
    def max_delimiter_priority(self): # pragma: no cover
        return self.priority # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    pass  # Assume some properties and methods for Leaf # pragma: no cover
 # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, type_: NodeType, children: List[Union['MockNode', Leaf]]): # pragma: no cover
        self.type = type_ # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
node = MockNode(Syms.atom, [Leaf(), Leaf()])  # Initialize with Leaf objects for simplicity # pragma: no cover
syms = Syms() # pragma: no cover
token = Token() # pragma: no cover

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
