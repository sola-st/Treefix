from typing import List, Any # pragma: no cover

class Mock: pass # pragma: no cover
class Leaf: pass # pragma: no cover
class BracketTracker: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.priority = 0 # pragma: no cover
    def mark(self, leaf): # pragma: no cover
        self.priority += 1 # pragma: no cover
    def max_delimiter_priority(self): # pragma: no cover
        if self.priority == 0: # pragma: no cover
            raise ValueError('No priority found') # pragma: no cover
        return self.priority # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, type, children): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children # pragma: no cover
syms = type('syms', (), {'atom': 'ATOM'})() # pragma: no cover
token = type('token', (), {'LPAR': '(', 'RPAR': ')'})() # pragma: no cover
node = Node('atom', [token.LPAR, Leaf(), Leaf(), token.RPAR]) # pragma: no cover

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
