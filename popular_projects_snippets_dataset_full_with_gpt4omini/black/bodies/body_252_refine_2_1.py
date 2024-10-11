from typing import List # pragma: no cover
class Leaf: pass # pragma: no cover
class BracketTracker: pass # pragma: no cover
class Node: pass # pragma: no cover
class Syms: pass # pragma: no cover
class Token: pass # pragma: no cover

node = Node() # pragma: no cover
syms = Syms() # pragma: no cover
token = Token() # pragma: no cover
BracketTracker = BracketTracker # pragma: no cover
Leaf = Leaf # pragma: no cover

from typing import List # pragma: no cover
class Leaf: pass # pragma: no cover
class BracketTracker: pass # pragma: no cover
class Node: pass # pragma: no cover
class Syms: pass # pragma: no cover
class Token: pass # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type, children):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children # pragma: no cover
class Syms:# pragma: no cover
    atom = 'atom' # pragma: no cover
class Token:# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
    RPAR = 'RPAR' # pragma: no cover
BracketTracker.max_delimiter_priority = lambda self: 1 # pragma: no cover
Leaf.leaves = lambda self: [Leaf()] # pragma: no cover

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
