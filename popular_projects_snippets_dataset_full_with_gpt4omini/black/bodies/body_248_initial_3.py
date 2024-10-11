from typing import List # pragma: no cover

class MockLeaf: pass # pragma: no cover
leaf = MockLeaf() # pragma: no cover
leaf.type = 'COLON' # pragma: no cover
class MockToken: COLON = 'COLON' # pragma: no cover
token = MockToken() # pragma: no cover
class MockSelf:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self._lambda_argument_depths = [1, 2, 3] # pragma: no cover
        self.depth = 2 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""See `maybe_increment_lambda_arguments` above for explanation."""
if (
    self._lambda_argument_depths
    and self._lambda_argument_depths[-1] == self.depth
    and leaf.type == token.COLON
):
    _l_(4845)

    self.depth -= 1
    _l_(4842)
    self._lambda_argument_depths.pop()
    _l_(4843)
    aux = True
    _l_(4844)
    exit(aux)
aux = False
_l_(4846)

exit(aux)
