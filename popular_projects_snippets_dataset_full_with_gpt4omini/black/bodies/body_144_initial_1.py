from typing import List # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
self = type('Mock', (object,), {'leaves': [Leaf(STANDALONE_COMMENT)]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a standalone comment?"""
aux = len(self.leaves) == 1 and self.leaves[0].type == STANDALONE_COMMENT
_l_(8284)
exit(aux)
