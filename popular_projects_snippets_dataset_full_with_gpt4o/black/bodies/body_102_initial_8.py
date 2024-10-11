import token # pragma: no cover
from typing import List # pragma: no cover
from collections.abc import Callable # pragma: no cover

class MockSymType: # pragma: no cover
    return_stmt = 'return_stmt' # pragma: no cover
    yield_expr = 'yield_expr' # pragma: no cover
 # pragma: no cover
syms = MockSymType() # pragma: no cover
 # pragma: no cover
def parent_type(leaf): # pragma: no cover
    return leaf.get('type', None) # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(lst): # pragma: no cover
    def is_valid_index(idx): # pragma: no cover
        return 0 <= idx < len(lst) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_empty_par(leaf): # pragma: no cover
    return leaf.get('type', None) == 'empty' # pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the return/yield statement
            requirements listed in the 'Requirements' section of this classes'
            docstring.
                OR
            None, otherwise.
        """
# If this line is apart of a return/yield statement and the first leaf
# contains either the "return" or "yield" keywords...
if parent_type(LL[0]) in [syms.return_stmt, syms.yield_expr] and LL[
    0
].value in ["return", "yield"]:
    _l_(20318)

    is_valid_index = is_valid_index_factory(LL)
    _l_(20314)

    idx = 2 if is_valid_index(1) and is_empty_par(LL[1]) else 1
    _l_(20315)
    # The next visible leaf MUST contain a string...
    if is_valid_index(idx) and LL[idx].type == token.STRING:
        _l_(20317)

        aux = idx
        _l_(20316)
        exit(aux)
aux = None
_l_(20319)

exit(aux)
