from typing import List, Union, Any # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.priority = 0# pragma: no cover
# pragma: no cover
    def max_delimiter_priority(self) -> int:# pragma: no cover
        return self.priority# pragma: no cover
class MockNode:# pragma: no cover
    pass
syms = type('syms', (object,), {'atom': 999}) # pragma: no cover
token = type('token', (object,), {'LPAR': 1, 'RPAR': 2}) # pragma: no cover

from typing import List, Union # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type_):# pragma: no cover
        self.type = type_# pragma: no cover
# pragma: no cover
    def mark(self, leaf):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
MockLeaf = MockLeaf # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.priority = 42  # Example priority value# pragma: no cover
# pragma: no cover
    def mark(self, leaf):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
    def max_delimiter_priority(self):# pragma: no cover
        return self.priority# pragma: no cover
# pragma: no cover
MockBracketTracker = MockBracketTracker # pragma: no cover
class MockNode:# pragma: no cover
    def __init__(self, type_, children):# pragma: no cover
        self.type = type_# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
MockNode = MockNode # pragma: no cover
node = MockNode(type_='atom', children=[MockLeaf(type_='('), MockLeaf(type_='content'), MockLeaf(type_=')')]) # pragma: no cover
syms = type('syms', (object,), {'atom': 'atom'}) # pragma: no cover
token = type('token', (object,), {'LPAR': '(', 'RPAR': ')'}) # pragma: no cover

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
