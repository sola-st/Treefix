from typing import List # pragma: no cover

leaf = type('Mock', (object,), {'type': 'TYPE_A', 'parent': type('MockParent', (object,), {'type': 'TYPE_B', 'parent': type('MockGrandparent', (object,), {'type': 'TYPE_C'})()})()})() # pragma: no cover
VARARGS_SPECIALS = {'TYPE_A', 'TYPE_X'} # pragma: no cover
syms = type('MockSyms', (object,), {'star_expr': 'TYPE_B'}) # pragma: no cover
within = {'TYPE_C', 'TYPE_D'} # pragma: no cover

leaf = type('Mock', (object,), {'type': 'type_a', 'parent': type('MockParent', (object,), {'type': 'type_b', 'parent': type('MockGrandparent', (object,), {'type': 'type_c'})()})()})() # pragma: no cover
VARARGS_SPECIALS = {'type_a', 'type_x'} # pragma: no cover
syms = type('MockSyms', (object,), {'star_expr': 'type_b'}) # pragma: no cover
within = {'type_c', 'type_d'} # pragma: no cover

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
    _l_(15485)

    aux = False
    _l_(15484)
    exit(aux)

p = leaf.parent
_l_(15486)
if p.type == syms.star_expr:
    _l_(15490)

    # Star expressions are also used as assignment targets in extended
    # iterable unpacking (PEP 3132).  See what its parent is instead.
    if not p.parent:
        _l_(15488)

        aux = False
        _l_(15487)
        exit(aux)

    p = p.parent
    _l_(15489)
aux = p.type in within
_l_(15491)

exit(aux)
