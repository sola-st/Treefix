from typing import List # pragma: no cover

class Mock(object): pass # pragma: no cover
self = type('Mock', (object,), {'leaves': [Mock()]})() # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves # pragma: no cover
self = Mock([None]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this an import line?"""
aux = bool(self) and is_import(self.leaves[0])
_l_(17761)
exit(aux)
