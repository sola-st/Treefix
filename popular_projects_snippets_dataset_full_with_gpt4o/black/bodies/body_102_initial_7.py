from typing import List, Callable, Any # pragma: no cover

def parent_type(node): return node['type'] # pragma: no cover
LL = [{'type': 1, 'value': 'return'}, {'type': 2, 'value': '""'}, {'type': 3, 'value': '"target_string"'}] # pragma: no cover
syms = type('MockSyms', (object,), {'return_stmt': 1, 'yield_expr': 2}) # pragma: no cover
def is_valid_index_factory(LL: List[dict]) -> Callable[[int], bool]: return lambda idx: 0 <= idx < len(LL) # pragma: no cover
def is_empty_par(node): return node['value'] == '""' # pragma: no cover
token = type('MockToken', (object,), {'STRING': 3}) # pragma: no cover

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
