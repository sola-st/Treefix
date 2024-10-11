from collections import namedtuple # pragma: no cover
import token # pragma: no cover

Mock = type('Mock', (object,), {}) # pragma: no cover
self = Mock # pragma: no cover
self.leaves = [] # pragma: no cover
token.COLON = token.COLON if hasattr(token, 'COLON') else 58 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Does this line open a new level of indentation."""
if len(self.leaves) == 0:
    _l_(15385)

    aux = False
    _l_(15384)
    exit(aux)
aux = self.leaves[-1].type == token.COLON
_l_(15386)
exit(aux)
