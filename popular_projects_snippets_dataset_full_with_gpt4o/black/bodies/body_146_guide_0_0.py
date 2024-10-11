import sys # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [Mock.Leaf()] # pragma: no cover
    @staticmethod # pragma: no cover
    class Leaf: # pragma: no cover
        def __init__(self): # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this an import line?"""
aux = bool(self) and is_import(self.leaves[0])
_l_(17761)
exit(aux)
