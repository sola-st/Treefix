import token # pragma: no cover

class MockLeaves: pass # pragma: no cover
self = type('Mock', (), {'leaves': [MockLeaves(), MockLeaves()]})() # pragma: no cover
token = type('MockToken', (), {'COLON': 'COLON'})() # pragma: no cover

import token # pragma: no cover

class MockLeaves:# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type # pragma: no cover
self = type('Mock', (), {'leaves': [MockLeaves(token.COLON)]})() # pragma: no cover
token = type('MockToken', (), {'COLON': 'COLON'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Does this line open a new level of indentation."""
if len(self.leaves) == 0:
    _l_(3775)

    aux = False
    _l_(3774)
    exit(aux)
aux = self.leaves[-1].type == token.COLON
_l_(3776)
exit(aux)
