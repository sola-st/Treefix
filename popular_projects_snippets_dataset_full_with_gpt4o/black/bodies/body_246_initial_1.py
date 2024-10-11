from collections import deque # pragma: no cover
from typing import Any # pragma: no cover

self = type('Mock', (object,), {'_for_loop_depths': deque([1]), 'depth': 1})() # pragma: no cover
leaf = type('Mock', (object,), {'type': 'NAME', 'value': 'in'})() # pragma: no cover
token = type('Mock', (object,), {'NAME': 'NAME'})() # pragma: no cover

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
