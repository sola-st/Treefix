class MockLeaf: pass # pragma: no cover
leaf = MockLeaf() # pragma: no cover
leaf.type = "some_type" # pragma: no cover
leaf.parent = MockLeaf() # pragma: no cover
VARARGS_SPECIALS = {"some_type"} # pragma: no cover
class MockSyms: pass # pragma: no cover
syms = MockSyms() # pragma: no cover
syms.star_expr = "star_expr" # pragma: no cover
within = {"some_within_type"} # pragma: no cover

class Mock: pass # pragma: no cover
leaf = Mock() # pragma: no cover
leaf.type = 'type_A' # pragma: no cover
leaf.parent = Mock() # pragma: no cover
leaf.parent.type = 'star_expr' # pragma: no cover
leaf.parent.parent = Mock() # pragma: no cover
leaf.parent.parent.type = 'some_within_type' # pragma: no cover
VARARGS_SPECIALS = {'type_A', 'other_type'} # pragma: no cover
syms = Mock() # pragma: no cover
syms.star_expr = 'star_expr' # pragma: no cover
within = {'some_within_type', 'another_within_type'} # pragma: no cover

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
