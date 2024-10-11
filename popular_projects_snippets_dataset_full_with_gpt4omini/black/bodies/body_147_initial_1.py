from typing import List # pragma: no cover
import token # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.leaves = [Mock()] # pragma: no cover
self.leaves[0].type = token.NAME # pragma: no cover
self.leaves[0].value = 'class' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a class definition?"""
aux = (
    bool(self)
    and self.leaves[0].type == token.NAME
    and self.leaves[0].value == "class"
)
_l_(6268)
exit(aux)
