import token # pragma: no cover

self = type('MockSelf', (object,), {'_lambda_argument_depths': [1], 'depth': 1})() # pragma: no cover
leaf = type('MockLeaf', (object,), {'type': token.COLON})() # pragma: no cover

import token # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._lambda_argument_depths = [1] # pragma: no cover
        self.depth = 1 # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
leaf = type('MockLeaf', (object,), {'type': token.COLON})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""See `maybe_increment_lambda_arguments` above for explanation."""
if (
    self._lambda_argument_depths
    and self._lambda_argument_depths[-1] == self.depth
    and leaf.type == token.COLON
):
    _l_(16610)

    self.depth -= 1
    _l_(16607)
    self._lambda_argument_depths.pop()
    _l_(16608)
    aux = True
    _l_(16609)
    exit(aux)
aux = False
_l_(16611)

exit(aux)
