from typing import Optional # pragma: no cover
from types import SimpleNamespace # pragma: no cover
import enum # pragma: no cover

class VARARGS_SPECIALS(enum.Enum): # pragma: no cover
    SPECIAL_1 = 1 # pragma: no cover
    SPECIAL_2 = 2 # pragma: no cover
    # Add other special types as necessary # pragma: no cover
 # pragma: no cover
class syms: # pragma: no cover
    star_expr = 1  # Dummy value for the star_expr symbol # pragma: no cover
 # pragma: no cover
within = {syms.star_expr}  # Dummy set of types within which the check is made # pragma: no cover
 # pragma: no cover
leaf = SimpleNamespace( # pragma: no cover
    type=VARARGS_SPECIALS.SPECIAL_1, # pragma: no cover
    parent=SimpleNamespace( # pragma: no cover
        type=syms.star_expr, # pragma: no cover
        parent=SimpleNamespace( # pragma: no cover
            type=syms.star_expr  # Can be None if applicable # pragma: no cover
        ) # pragma: no cover
    ) # pragma: no cover
) # pragma: no cover

class MockParent: # pragma: no cover
    def __init__(self, type, parent=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.parent = parent # pragma: no cover
 # pragma: no cover
leaf = MockParent(type='VARARGS_TYPE_1', parent=MockParent(type='star_expr', parent=MockParent(type='some_type'))) # pragma: no cover
VARARGS_SPECIALS = {'VARARGS_TYPE_1', 'VARARGS_TYPE_2'} # pragma: no cover
syms = type('MockSyms', (object,), {'star_expr': 'star_expr'}) # pragma: no cover
within = {'some_type', 'another_type'} # pragma: no cover

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
