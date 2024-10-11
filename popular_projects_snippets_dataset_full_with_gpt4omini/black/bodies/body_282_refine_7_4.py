from typing import Optional, List # pragma: no cover

class Node:  # Definition of a mock Node class# pragma: no cover
    def __init__(self, type: str, prev_sibling: Optional['Node'] = None):# pragma: no cover
        self.type = type# pragma: no cover
        self.prev_sibling = prev_sibling# pragma: no cover
# pragma: no cover
# Creating a mock node with type 'A' and a previous sibling of type 'B'# pragma: no cover
node = Node('A', Node('B')) # pragma: no cover
tokens = ['B', 'A'] # pragma: no cover
def prev_siblings_are(node: Optional[Node], tokens: List[str]) -> bool:# pragma: no cover
    if node is None:# pragma: no cover
        return len(tokens) == 0# pragma: no cover
    return node.type == tokens.pop(0) and prev_siblings_are(node.prev_sibling, tokens)# pragma: no cover
 # pragma: no cover

from typing import List, Optional # pragma: no cover

class Node:# pragma: no cover
    def __init__(self, type: str, prev_sibling: Optional['Node'] = None):# pragma: no cover
        self.type = type# pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
node = Node(type='A', prev_sibling=Node(type='B')) # pragma: no cover
tokens = ['B', 'A'] # pragma: no cover
def prev_siblings_are(node: Optional[Node], tokens: List[str]) -> bool:# pragma: no cover
    if not tokens:# pragma: no cover
        return node is None# pragma: no cover
    if node is None:# pragma: no cover
        return False# pragma: no cover
    if node.type != tokens[0]:# pragma: no cover
        return False# pragma: no cover
    return prev_siblings_are(node.prev_sibling, tokens[1:]) # pragma: no cover

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
