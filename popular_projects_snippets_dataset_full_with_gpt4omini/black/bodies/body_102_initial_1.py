from typing import List, Optional, Callable, Any # pragma: no cover
import tokenize # pragma: no cover

syms = type('Mock', (object,), {'return_stmt': 'return_stmt', 'yield_expr': 'yield_expr'})() # pragma: no cover
token = type('Mock', (object,), {'STRING': 'string'})() # pragma: no cover
LL: List[Any] = [type('MockLeaf', (object,), {'type': 'string', 'value': 'yield'})()] * 3 # pragma: no cover
parent_type = lambda x: x.type # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_empty_par = lambda leaf: leaf.value == '' # pragma: no cover

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
