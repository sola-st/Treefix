VARARGS_SPECIALS = {'VARARGS_TYPE_1', 'VARARGS_TYPE_2'} # pragma: no cover
syms = type('Mock', (object,), {'star_expr': 'star_expression_type'}) # pragma: no cover
within = {'some_type', 'another_type', 'yet_another_type'} # pragma: no cover
leaf = type('Mock', (object,), {'type': 'VARARGS_TYPE_1', 'parent': type('Mock', (object,), {'type': 'star_expression_type', 'parent': type('Mock', (object,), {'type': 'some_type'})()})()})() # pragma: no cover

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
