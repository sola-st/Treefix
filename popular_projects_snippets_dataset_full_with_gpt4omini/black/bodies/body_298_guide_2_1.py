from collections import namedtuple # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self, type, parent=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.parent = parent # pragma: no cover
VARARGS_SPECIALS = ['star_expr', 'double_star_expr'] # pragma: no cover
node = MockNode(type='not_a_star', parent=None) # pragma: no cover
leaf = MockNode(type='some_type', parent=node) # pragma: no cover
syms = type('MockSyms', (), {'star_expr': 'star_expr'})() # pragma: no cover
within = ['another_expression'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `leaf` is a star or double star in a vararg or kwarg.

    If `within` includes VARARGS_PARENTS, this applies to function signatures.
    If `within` includes UNPACKING_PARENTS, it applies to right hand-side
    extended iterable unpacking (PEP 3132) and additional unpacking
    generalizations (PEP 448).
    """
if leaf.type not in VARARGS_SPECIALS or not leaf.parent:
    _l_(3913)

    aux = False
    _l_(3912)
    exit(aux)

p = leaf.parent
_l_(3914)
if p.type == syms.star_expr:
    _l_(3918)

    # Star expressions are also used as assignment targets in extended
    # iterable unpacking (PEP 3132).  See what its parent is instead.
    if not p.parent:
        _l_(3916)

        aux = False
        _l_(3915)
        exit(aux)

    p = p.parent
    _l_(3917)
aux = p.type in within
_l_(3919)

exit(aux)
