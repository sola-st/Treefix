from typing import Optional # pragma: no cover
import token # pragma: no cover

from typing import Optional # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [Leaf(token.NAME, 'def'), Leaf(token.NAME, 'def')] # pragma: no cover
self = MockSelf() # pragma: no cover
token.NAME = 1 # pragma: no cover
token.ASYNC = 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this a function definition? (Also returns True for async defs.)"""
try:
    _l_(7217)

    first_leaf = self.leaves[0]
    _l_(7214)
except IndexError:
    _l_(7216)

    aux = False
    _l_(7215)
    exit(aux)

try:
    _l_(7221)

    second_leaf: Optional[Leaf] = self.leaves[1]
    _l_(7218)
except IndexError:
    _l_(7220)

    second_leaf = None
    _l_(7219)
aux = (first_leaf.type == token.NAME and first_leaf.value == "def") or (
    first_leaf.type == token.ASYNC
    and second_leaf is not None
    and second_leaf.type == token.NAME
    and second_leaf.value == "def"
)
_l_(7222)
exit(aux)
