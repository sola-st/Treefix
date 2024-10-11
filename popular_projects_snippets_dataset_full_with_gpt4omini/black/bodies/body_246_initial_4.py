import token # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
leaf = MockLeaf(token.NAME, 'in') # pragma: no cover
self = type('Mock', (object,), {'_for_loop_depths': [1], 'depth': 1})() # pragma: no cover

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
    _l_(7973)

    self.depth -= 1
    _l_(7970)
    self._for_loop_depths.pop()
    _l_(7971)
    aux = True
    _l_(7972)
    exit(aux)
aux = False
_l_(7974)

exit(aux)
