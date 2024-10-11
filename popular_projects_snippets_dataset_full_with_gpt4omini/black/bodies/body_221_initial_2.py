from typing import List, Optional # pragma: no cover

class Child:  # a class to represent a child with a leaf# pragma: no cover
    def __init__(self, name):# pragma: no cover
        self.name = name# pragma: no cover
    # pragma: no cover
class Container:# pragma: no cover
    def __init__(self, children):# pragma: no cover
        self.children = children# pragma: no cover
# pragma: no cover
child1 = Child('child1')# pragma: no cover
child2 = Child('child2')# pragma: no cover
container = Container([child1, child2])# pragma: no cover
# pragma: no cover
# Mock method to get the first leaf of a child# pragma: no cover
def first_leaf_of(child):# pragma: no cover
    return child if isinstance(child, Child) else None# pragma: no cover
# pragma: no cover
# Mock method to determine if formatting is on# pragma: no cover
def is_fmt_on(leaf, preview):# pragma: no cover
    return True if preview else False# pragma: no cover
# pragma: no cover
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
