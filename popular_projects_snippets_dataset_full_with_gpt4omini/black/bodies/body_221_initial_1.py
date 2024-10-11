from typing import Optional, List # pragma: no cover

class MockChild:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.children = []# pragma: no cover
# pragma: no cover
class MockContainer:# pragma: no cover
    def __init__(self, children):# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
container = MockContainer(children=[MockChild(), MockChild()]) # pragma: no cover
def first_leaf_of(child):# pragma: no cover
    return child if isinstance(child, MockChild) else None # pragma: no cover
def is_fmt_on(leaf, preview=False):# pragma: no cover
    return preview # pragma: no cover
preview = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Determine if children have formatting switched on."""
for child in container.children:
    _l_(7951)

    leaf = first_leaf_of(child)
    _l_(7948)
    if leaf is not None and is_fmt_on(leaf, preview=preview):
        _l_(7950)

        aux = True
        _l_(7949)
        exit(aux)
aux = False
_l_(7952)

exit(aux)
