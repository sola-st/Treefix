import sys # pragma: no cover
from typing import List # pragma: no cover

node = type('MockNode', (object,), {'type': 'atom', 'children': []})() # pragma: no cover
syms = type('MockSyms', (object,), {'atom': 'atom'}) # pragma: no cover
token = type('MockToken', (object,), {'LPAR': '(', 'RPAR': ')'}) # pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'mark': lambda self, x: None, 'max_delimiter_priority': lambda self: 1}) # pragma: no cover
Leaf = type('MockLeaf', (object,), {}) # pragma: no cover
bt = BracketTracker() # pragma: no cover
first = type('MockFirst', (object,), {'type': '(', 'children': []})() # pragma: no cover
last = type('MockLast', (object,), {'type': ')', 'children': []})() # pragma: no cover
node.children = [first, last] # pragma: no cover

import sys # pragma: no cover
from typing import List # pragma: no cover

Leaf = type('Leaf', (object,), {'__init__': lambda self, type_: setattr(self, 'type', type_)}) # pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'__init__': lambda self: setattr(self, 'delimiters', []), 'mark': lambda self, leaf: self.delimiters.append(leaf), 'max_delimiter_priority': lambda self: 10 if self.delimiters else ValueError('No delimiters')}) # pragma: no cover
syms = type('syms', (object,), {'atom': 'atom'}) # pragma: no cover
token = type('token', (object,), {'LPAR': 'LPAR', 'RPAR': 'RPAR'}) # pragma: no cover

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
