from collections import namedtuple # pragma: no cover
import token # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'value']) # pragma: no cover
self = type('MockSelf', (object,), {'is_class': True, 'leaves': [Leaf(token.DOT, '.'), Leaf(token.DOT, '.'), Leaf(token.DOT, '.')]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a class definition with a body consisting only of "..."?"""
aux = self.is_class and self.leaves[-3:] == [
    Leaf(token.DOT, ".") for _ in range(3)
]
_l_(15822)
exit(aux)
