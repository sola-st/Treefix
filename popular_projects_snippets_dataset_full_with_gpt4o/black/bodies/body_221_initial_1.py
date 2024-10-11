from typing import List, Optional # pragma: no cover

class MockChild:# pragma: no cover
    def __init__(self, name):# pragma: no cover
        self.name = name# pragma: no cover
# pragma: no cover
class MockContainer:# pragma: no cover
    def __init__(self, children: List[MockChild]):# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
container = MockContainer(children=[MockChild('child1'), MockChild('child2')]) # pragma: no cover
def first_leaf_of(child: MockChild) -> Optional[str]:# pragma: no cover
    return 'leaf' if child.name == 'child1' else None # pragma: no cover
def is_fmt_on(leaf: str, preview: bool) -> bool:# pragma: no cover
    return preview # pragma: no cover
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
