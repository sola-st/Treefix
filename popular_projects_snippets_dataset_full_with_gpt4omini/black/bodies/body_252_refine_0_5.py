from typing import List, Union # pragma: no cover
class Mock: pass # pragma: no cover
class Leaf: pass # pragma: no cover
class BracketTracker: pass # pragma: no cover
import token # pragma: no cover

node = Mock() # pragma: no cover
node.children = [Mock(), Mock()] # pragma: no cover
node.children[0].type = token.LPAR # pragma: no cover
node.children[1].type = token.RPAR # pragma: no cover
token.LPAR = 'LPAR' # pragma: no cover
token.RPAR = 'RPAR' # pragma: no cover
BracketTracker.max_delimiter_priority = lambda self: 1 # pragma: no cover
Leaf.leaves = lambda self: [Mock()] # pragma: no cover

from typing import List, Union # pragma: no cover

class Mock: pass # pragma: no cover
class Leaf: pass # pragma: no cover
class BracketTracker: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.marked_leaves = [] # pragma: no cover
    def mark(self, leaf): # pragma: no cover
        self.marked_leaves.append(leaf) # pragma: no cover
    def max_delimiter_priority(self): # pragma: no cover
        if not self.marked_leaves: # pragma: no cover
            raise ValueError('No leaves marked') # pragma: no cover
        return 1 # pragma: no cover
node = Mock() # pragma: no cover
node.type = 'atom' # pragma: no cover
node.children = [Mock(), Mock()] # pragma: no cover
node.children[0].type = 'LPAR' # pragma: no cover
node.children[1].type = 'RPAR' # pragma: no cover
syms = Mock() # pragma: no cover
syms.atom = 'atom' # pragma: no cover
token = Mock() # pragma: no cover
token.LPAR = 'LPAR' # pragma: no cover
token.RPAR = 'RPAR' # pragma: no cover
Leaf.leaves = lambda self: [Mock()] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""Return maximum delimiter priority inside `node`.

    This is specific to atoms with contents contained in a pair of parentheses.
    If `node` isn't an atom or there are no enclosing parentheses, returns 0.
    """
if node.type != syms.atom:
    _l_(7955)

    aux = 0
    _l_(7954)
    exit(aux)

first = node.children[0]
_l_(7956)
last = node.children[-1]
_l_(7957)
if not (first.type == token.LPAR and last.type == token.RPAR):
    _l_(7959)

    aux = 0
    _l_(7958)
    exit(aux)

bt = BracketTracker()
_l_(7960)
for c in node.children[1:-1]:
    _l_(7965)

    if isinstance(c, Leaf):
        _l_(7964)

        bt.mark(c)
        _l_(7961)
    else:
        for leaf in c.leaves():
            _l_(7963)

            bt.mark(leaf)
            _l_(7962)
try:
    _l_(7969)

    aux = bt.max_delimiter_priority()
    _l_(7966)
    exit(aux)

except ValueError:
    _l_(7968)

    aux = 0
    _l_(7967)
    exit(aux)
