from typing import List, Optional # pragma: no cover
import token # pragma: no cover
from collections import namedtuple # pragma: no cover

syms = type('Mock', (object,), {'return_stmt': 1, 'yield_expr': 2})() # pragma: no cover
LL: List = [type('MockLeaf', (object,), {'type': token.STRING, 'value': 'return'})()] * 3 # pragma: no cover
parent_type = lambda x: syms.return_stmt if LL[x].value == 'return' else syms.yield_expr # pragma: no cover
is_valid_index_factory = lambda ll: lambda idx: 0 <= idx < len(ll) # pragma: no cover
is_valid_index = is_valid_index_factory(LL) # pragma: no cover
is_empty_par = lambda leaf: isinstance(leaf, type('MockLeaf', (object,), {})) # pragma: no cover
token = type('MockToken', (object,), {'STRING': 3})() # pragma: no cover

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
