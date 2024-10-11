from typing import List, Any # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type, children):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children # pragma: no cover
class MockSyms:# pragma: no cover
    atom = 'atom' # pragma: no cover
class MockToken:# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
    RPAR = 'RPAR' # pragma: no cover
class BracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.priorities = []# pragma: no cover
    def mark(self, leaf):# pragma: no cover
        pass# pragma: no cover
    def max_delimiter_priority(self):# pragma: no cover
        if not self.priorities:# pragma: no cover
            raise ValueError# pragma: no cover
        return max(self.priorities) # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, content):# pragma: no cover
        self.content = content # pragma: no cover

from typing import List # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type: str, children: List):# pragma: no cover
        self.type = type# pragma: no cover
        self.children = children # pragma: no cover
class MockSyms:# pragma: no cover
    atom = 'atom' # pragma: no cover
class MockToken:# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
    RPAR = 'RPAR' # pragma: no cover
class BracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.marked = []# pragma: no cover
    def mark(self, leaf):# pragma: no cover
        self.marked.append(leaf)# pragma: no cover
    def max_delimiter_priority(self):# pragma: no cover
        return len(self.marked) or 1 # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self):# pragma: no cover
        pass# pragma: no cover
    def leaves(self):# pragma: no cover
        return [self] # pragma: no cover
node = MockNode('atom', [MockNode('LPAR', []), Leaf(), Leaf(), MockNode('RPAR', [])]) # pragma: no cover
syms = MockSyms() # pragma: no cover
token = MockToken() # pragma: no cover

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
