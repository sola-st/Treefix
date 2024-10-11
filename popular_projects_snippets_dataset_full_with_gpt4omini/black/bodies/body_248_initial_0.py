from typing import List # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, token_type):# pragma: no cover
        self.type = token_type # pragma: no cover
class MockToken:# pragma: no cover
    COLON = ':' # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._lambda_argument_depths = [1]# pragma: no cover
        self.depth = 1# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
token = MockToken() # pragma: no cover

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
