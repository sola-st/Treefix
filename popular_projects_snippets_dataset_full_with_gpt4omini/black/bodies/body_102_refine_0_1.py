from typing import List, Optional # pragma: no cover
import enum # pragma: no cover

class Mock: pass # pragma: no cover
syms = type('MockSYMS', (object,), {'return_stmt': 1, 'yield_expr': 2})() # pragma: no cover
token = type('MockToken', (object,), {'STRING': 3})() # pragma: no cover
LL = [Mock(), Mock(), Mock()] # pragma: no cover
LL[0].value = 'return' # pragma: no cover
LL[1].type = token.STRING # pragma: no cover
LL[1].value = 'target_string' # pragma: no cover
def parent_type(node): return syms.return_stmt # pragma: no cover
def is_valid_index_factory(LL): return lambda idx: 0 <= idx < len(LL) # pragma: no cover
def is_empty_par(node): return len(node) == 0 # pragma: no cover

from typing import List, Optional # pragma: no cover
import enum # pragma: no cover

class Mock: pass # pragma: no cover

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
    _l_(8776)

    is_valid_index = is_valid_index_factory(LL)
    _l_(8772)

    idx = 2 if is_valid_index(1) and is_empty_par(LL[1]) else 1
    _l_(8773)
    # The next visible leaf MUST contain a string...
    if is_valid_index(idx) and LL[idx].type == token.STRING:
        _l_(8775)

        aux = idx
        _l_(8774)
        exit(aux)
aux = None
_l_(8777)

exit(aux)
