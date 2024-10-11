import token # pragma: no cover

class MockLeaves:  # Mock class to simulate leaves# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
# pragma: no cover
self = MockSelf([])  # Initialize with no leaves# pragma: no cover
aux = False  # This line is to make sure aux is defined before usage # pragma: no cover

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
