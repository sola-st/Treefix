from typing import List # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self._for_loop_depths: List[int] = [1] # pragma: no cover
self.depth = 1 # pragma: no cover
leaf = Mock() # pragma: no cover
token = Mock() # pragma: no cover
leaf.type = token.NAME # pragma: no cover
token.NAME = 'NAME' # pragma: no cover
leaf.value = 'in' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""See `maybe_increment_for_loop_variable` above for explanation."""
if (
    self._for_loop_depths
    and self._for_loop_depths[-1] == self.depth
    and leaf.type == token.NAME
    and leaf.value == "in"
):
    _l_(19749)

    self.depth -= 1
    _l_(19746)
    self._for_loop_depths.pop()
    _l_(19747)
    aux = True
    _l_(19748)
    exit(aux)
aux = False
_l_(19750)

exit(aux)
