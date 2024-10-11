import token # pragma: no cover

self = type('Mock', (object,), {'leaves': [type('Leaf', (object,), {'type': token.AT})()]})() # pragma: no cover
token.AT = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a decorator?"""
aux = bool(self) and self.leaves[0].type == token.AT
_l_(18430)
exit(aux)
