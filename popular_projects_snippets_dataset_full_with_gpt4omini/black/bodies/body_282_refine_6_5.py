from typing import List, Optional # pragma: no cover

class MockNode(object): # pragma: no cover
    def __init__(self, type=None, prev_sibling=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.prev_sibling = prev_sibling # pragma: no cover
 # pragma: no cover
class MockSibling(object): # pragma: no cover
    def __init__(self, type=None): # pragma: no cover
        self.type = type # pragma: no cover
 # pragma: no cover
node = MockNode(type='A', prev_sibling=MockNode(type='B')) # pragma: no cover
tokens = ['B', 'A'] # pragma: no cover
def prev_siblings_are(node, tokens): # pragma: no cover
    while node is not None and tokens: # pragma: no cover
        if node.type != tokens.pop(0): # pragma: no cover
            return False # pragma: no cover
        node = node.prev_sibling # pragma: no cover
    return not tokens # pragma: no cover

from typing import List, Optional # pragma: no cover

class Node:  # Mock class to simulate nodes # pragma: no cover
    def __init__(self, type=None, prev_sibling=None): # pragma: no cover
        self.type = type  # Node type # pragma: no cover
        self.prev_sibling = prev_sibling  # Reference to previous sibling # pragma: no cover
 # pragma: no cover
node = Node(type='A', prev_sibling=Node(type='B'))  # Create a test node with a previous sibling # pragma: no cover
tokens = ['B', 'A']  # Tokens representing expected sibling and node type # pragma: no cover
 # pragma: no cover
def prev_siblings_are(node, tokens):  # Function to check previous siblings against tokens # pragma: no cover
    for token in tokens[::-1]:  # Reverse tokens to check from last to first # pragma: no cover
        if node is None or node.type != token: # pragma: no cover
            return False # pragma: no cover
        node = node.prev_sibling  # Move to the previous sibling # pragma: no cover
    return True  # All checks passed # pragma: no cover

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
