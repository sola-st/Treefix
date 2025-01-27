# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a class definition with a body consisting only of "..."?"""
aux = self.is_class and self.leaves[-3:] == [
    Leaf(token.DOT, ".") for _ in range(3)
]
_l_(15822)
exit(aux)
