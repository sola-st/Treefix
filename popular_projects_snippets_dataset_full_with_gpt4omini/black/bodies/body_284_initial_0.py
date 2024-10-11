from typing import Optional # pragma: no cover

class LN:# pragma: no cover
    def __init__(self, parent=None):# pragma: no cover
        self.parent = parent # pragma: no cover
ancestor = LN() # pragma: no cover
descendant = LN(parent=ancestor) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return the child of `ancestor` that contains `descendant`."""
node: Optional[LN] = descendant
_l_(7297)
while node and node.parent != ancestor:
    _l_(7299)

    node = node.parent
    _l_(7298)
aux = node
_l_(7300)
exit(aux)
