import token # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type# pragma: no cover
    def leaves(self):# pragma: no cover
        return [self] # pragma: no cover
class BracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.delimiters = []# pragma: no cover
    def mark(self, leaf):# pragma: no cover
        if leaf.type in {token.LPAR, token.RPAR}:# pragma: no cover
            self.delimiters.append(leaf.type)# pragma: no cover
    def max_delimiter_priority(self):# pragma: no cover
        if not self.delimiters:# pragma: no cover
            raise ValueError('No delimiters')# pragma: no cover
        return 10 # pragma: no cover
syms = SimpleNamespace(atom=1) # pragma: no cover
node = SimpleNamespace(type=1, children=[Leaf(token.LPAR), Leaf('child'), Leaf(token.RPAR)]) # pragma: no cover

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
