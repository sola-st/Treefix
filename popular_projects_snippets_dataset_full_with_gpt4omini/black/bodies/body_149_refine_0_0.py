from typing import Optional # pragma: no cover
import tokenize # pragma: no cover
from collections import namedtuple # pragma: no cover

token = type('MockToken', (object,), {'NAME': 'NAME', 'ASYNC': 'ASYNC'})() # pragma: no cover

from typing import Optional # pragma: no cover
import tokenize # pragma: no cover
from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
class MockSelf: pass # pragma: no cover
self = MockSelf() # pragma: no cover
self.leaves = [Leaf('NAME', 'def'), Leaf('NAME', 'not_def')] # pragma: no cover
class MockToken: pass # pragma: no cover
token = MockToken() # pragma: no cover
token.NAME = 'NAME' # pragma: no cover
token.ASYNC = 'ASYNC' # pragma: no cover

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
