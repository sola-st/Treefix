import sys # pragma: no cover

class MockLeaf: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    leaves = [MockLeaf()] # pragma: no cover
 # pragma: no cover
    return isinstance(leaf, MockLeaf) # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this an import line?"""
aux = bool(self) and is_import(self.leaves[0])
_l_(17761)
exit(aux)
