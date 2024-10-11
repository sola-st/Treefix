from typing import Optional # pragma: no cover
import token # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type_, value): # pragma: no cover
        self.type = type_ # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
first_leaf = Leaf(token.NAME, 'def') # pragma: no cover
second_leaf = Leaf(token.NAME, 'def') # pragma: no cover
 # pragma: no cover
self = MockSelf([first_leaf, second_leaf]) # pragma: no cover

from typing import Optional # pragma: no cover
import token # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type_, value): # pragma: no cover
        self.type = type_ # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
Leaf = Leaf # pragma: no cover
 # pragma: no cover
first_leaf = Leaf(token.NAME, 'def') # pragma: no cover
second_leaf = Leaf(token.NAME, 'def') # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'leaves': [first_leaf, second_leaf]})() # pragma: no cover
token.NAME = 1 # pragma: no cover
token.ASYNC = 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this a function definition? (Also returns True for async defs.)"""
try:
    _l_(19180)

    first_leaf = self.leaves[0]
    _l_(19177)
except IndexError:
    _l_(19179)

    aux = False
    _l_(19178)
    exit(aux)

try:
    _l_(19184)

    second_leaf: Optional[Leaf] = self.leaves[1]
    _l_(19181)
except IndexError:
    _l_(19183)

    second_leaf = None
    _l_(19182)
aux = (first_leaf.type == token.NAME and first_leaf.value == "def") or (
    first_leaf.type == token.ASYNC
    and second_leaf is not None
    and second_leaf.type == token.NAME
    and second_leaf.value == "def"
)
_l_(19185)
exit(aux)
