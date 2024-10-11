from typing import Optional, List # pragma: no cover

class MockNode:  # Mock for the node with type attribute and prev_sibling method# pragma: no cover
    def __init__(self, type: str, prev_sibling: 'Optional[MockNode]' = None):# pragma: no cover
        self.type = type# pragma: no cover
        self.prev_sibling = prev_sibling# pragma: no cover
# pragma: no cover
node = MockNode(type='A', prev_sibling=None)  # Example node with type 'A' and no previous sibling # pragma: no cover
tokens = ['B', 'C', 'A']  # Example tokens list to match against # pragma: no cover
def prev_siblings_are(node: Optional[MockNode], tokens: List[str]) -> bool:  # Mock function for previous siblings check# pragma: no cover
    # This mock simply returns True if the left side matches the tokens length# pragma: no cover
    count = 0# pragma: no cover
    while node and count < len(tokens) - 1:# pragma: no cover
        if node.type != tokens[count]:# pragma: no cover
            return False# pragma: no cover
        count += 1# pragma: no cover
        node = node.prev_sibling# pragma: no cover
    return count == len(tokens) - 1  # Match if all tokens have been checked # pragma: no cover

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
