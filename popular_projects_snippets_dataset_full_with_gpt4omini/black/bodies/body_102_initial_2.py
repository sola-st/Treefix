from typing import List, Optional # pragma: no cover
import token # pragma: no cover
import builtins # pragma: no cover

def parent_type(node): return node['type'] # pragma: no cover
LL = [{'type': token.STRING, 'value': 'target'}, {'type': 'empty'}, {'type': token.STRING, 'value': 'matched'}] # pragma: no cover
class MockSyms: return_stmt = 'return_stmt'; yield_expr = 'yield_expr' # pragma: no cover
syms = MockSyms() # pragma: no cover
def is_valid_index_factory(LL): return lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_valid_index = is_valid_index_factory(LL) # pragma: no cover
def is_empty_par(node): return node['type'] == 'empty' # pragma: no cover

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
