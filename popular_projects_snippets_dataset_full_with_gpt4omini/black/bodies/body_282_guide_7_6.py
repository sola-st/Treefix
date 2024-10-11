from typing import List, Optional # pragma: no cover

class Node:  # Mock class for a node# pragma: no cover
    def __init__(self, node_type: Optional[str] = None, prev_sibling=None):# pragma: no cover
        self.type = node_type# pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
def prev_siblings_are(prev_sibling: Optional[Node], tokens: List[Optional[str]]) -> bool:# pragma: no cover
    return True  # Mock implementation for checking previous siblings # pragma: no cover
tokens: List[Optional[str]] = []  # Initialize tokens as an empty list to trigger the first condition # pragma: no cover
node: Optional[Node] = None  # Set node to None to trigger the 'if not node:' condition # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return if the `node` and its previous siblings match types against the provided
    list of tokens; the provided `node`has its type matched against the last element in
    the list.  `None` can be used as the first element to declare that the start of the
    list is anchored at the start of its parent's children."""
if not tokens:
    _l_(6544)

    aux = True
    _l_(6543)
    exit(aux)
if tokens[-1] is None:
    _l_(6546)

    aux = node is None
    _l_(6545)
    exit(aux)
if not node:
    _l_(6548)

    aux = False
    _l_(6547)
    exit(aux)
if node.type != tokens[-1]:
    _l_(6550)

    aux = False
    _l_(6549)
    exit(aux)
aux = prev_siblings_are(node.prev_sibling, tokens[:-1])
_l_(6551)
exit(aux)
