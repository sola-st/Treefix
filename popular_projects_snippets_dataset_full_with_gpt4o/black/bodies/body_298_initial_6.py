from typing import List # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type_value, parent_value=None):# pragma: no cover
        self.type = type_value# pragma: no cover
        self.parent = parent_value# pragma: no cover
# pragma: no cover
leaf = MockLeaf(type_value='desired_type', parent_value='mock_parent') # pragma: no cover
VARARGS_SPECIALS = {'special_type_1', 'special_type_2'} # pragma: no cover
syms = type('MockSyms', (object,), {'star_expr': 'star_expression_type'}) # pragma: no cover
within = {'within_type_1', 'within_type_2'} # pragma: no cover

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
