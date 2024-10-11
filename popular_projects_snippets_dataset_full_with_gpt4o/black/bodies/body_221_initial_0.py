from typing import List # pragma: no cover

class MockChild:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
class MockContainer:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.children: List[MockChild] = []# pragma: no cover
# pragma: no cover
container = MockContainer()# pragma: no cover
# pragma: no cover
# Adding mock child elements to the container# pragma: no cover
for _ in range(3):# pragma: no cover
    container.children.append(MockChild()) # pragma: no cover
def first_leaf_of(child):# pragma: no cover
    # Assuming first_leaf_of returns a string representing the leaf for the purpose of this example# pragma: no cover
    return 'leaf' if child else None # pragma: no cover
def is_fmt_on(leaf, preview):# pragma: no cover
    # Assuming a simple format check based on the leaf and preview values, returning True/False# pragma: no cover
    return leaf == 'leaf' and preview == True # pragma: no cover
preview = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Determine if children have formatting switched on."""
for child in container.children:
    _l_(19744)

    leaf = first_leaf_of(child)
    _l_(19741)
    if leaf is not None and is_fmt_on(leaf, preview=preview):
        _l_(19743)

        aux = True
        _l_(19742)
        exit(aux)
aux = False
_l_(19745)

exit(aux)
