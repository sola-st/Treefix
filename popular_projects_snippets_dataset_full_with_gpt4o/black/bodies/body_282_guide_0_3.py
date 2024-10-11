from typing import List, Optional, Any # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self, type: Optional[str] = None, prev_sibling: Optional["MockNode"] = None): # pragma: no cover
        self.type = type # pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
 # pragma: no cover
def prev_siblings_are(node: Optional[MockNode], tokens: List[Optional[str]]) -> bool: # pragma: no cover
    for token in reversed(tokens): # pragma: no cover
        if node is None: # pragma: no cover
            if token is not None: # pragma: no cover
                return False # pragma: no cover
        elif node.type != token: # pragma: no cover
            return False # pragma: no cover
        node = node.prev_sibling # pragma: no cover
    return True # pragma: no cover
 # pragma: no cover
tokens = [] # pragma: no cover
node = MockNode() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return if the `node` and its previous siblings match types against the provided
    list of tokens; the provided `node`has its type matched against the last element in
    the list.  `None` can be used as the first element to declare that the start of the
    list is anchored at the start of its parent's children."""
if not tokens:
    _l_(18322)

    aux = True
    _l_(18321)
    exit(aux)
if tokens[-1] is None:
    _l_(18324)

    aux = node is None
    _l_(18323)
    exit(aux)
if not node:
    _l_(18326)

    aux = False
    _l_(18325)
    exit(aux)
if node.type != tokens[-1]:
    _l_(18328)

    aux = False
    _l_(18327)
    exit(aux)
aux = prev_siblings_are(node.prev_sibling, tokens[:-1])
_l_(18329)
exit(aux)
