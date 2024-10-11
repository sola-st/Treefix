from typing import List # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
class Mock:# pragma: no cover
    is_class = True# pragma: no cover
    leaves = [Leaf('DOT', '.'), Leaf('DOT', '.'), Leaf('DOT', '.')]  # Simulating a list of leaves # pragma: no cover
token = type('MockToken', (), {'DOT': 'DOT'}) # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a class definition with a body consisting only of "..."?"""
aux = self.is_class and self.leaves[-3:] == [
    Leaf(token.DOT, ".") for _ in range(3)
]
_l_(4289)
exit(aux)
