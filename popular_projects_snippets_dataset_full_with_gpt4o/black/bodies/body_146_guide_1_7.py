import sys # pragma: no cover

class MockLeaf: # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
    def __bool__(self): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
 # pragma: no cover
self = MockSelf([MockLeaf(True)]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this an import line?"""
aux = bool(self) and is_import(self.leaves[0])
_l_(17761)
exit(aux)
