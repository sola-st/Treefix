import token # pragma: no cover

self = type('Mock', (object,), {'leaves': [{'type': token.COLON}]})() # pragma: no cover
token.COLON = 1 # pragma: no cover

import token # pragma: no cover

class MockLeaf:  # Mock class to simulate the leaf objects# pragma: no cover
    def __init__(self, leaf_type):# pragma: no cover
        self.type = leaf_type# pragma: no cover
# pragma: no cover
self = type('Mock', (object,), {'leaves': [MockLeaf(token.COLON)]})() # pragma: no cover
token.COLON = 1 # pragma: no cover

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
