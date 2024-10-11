from typing import List, Optional # pragma: no cover

class MockContainer:  # Mock for the container class # pragma: no cover
    def __init__(self, children: List): # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
def first_leaf_of(child):  # Mock for the first_leaf_of function # pragma: no cover
    return child if child in ['leaf1', 'leaf2'] else None # pragma: no cover
 # pragma: no cover
def is_fmt_on(leaf, preview):  # Mock for the is_fmt_on function # pragma: no cover
    return leaf in ['leaf1'] and preview # pragma: no cover
 # pragma: no cover
preview = True # pragma: no cover
container = MockContainer(children=['leaf1', 'branch1', 'leaf2']) # pragma: no cover

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
