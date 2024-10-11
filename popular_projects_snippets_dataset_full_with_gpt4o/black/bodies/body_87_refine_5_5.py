from typing import List, Optional # pragma: no cover
import token # pragma: no cover

class TErr(Exception):# pragma: no cover
    def __init__(self, message: str):# pragma: no cover
        super().__init__(message)# pragma: no cover
# pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = []# pragma: no cover
# pragma: no cover
line = MockLine() # pragma: no cover
class MockSelf:# pragma: no cover
    STRING_OPERATORS = [token.PLUS, token.MINUS]# pragma: no cover
    def _prefer_paren_wrap_match(self, leaves: List) -> Optional[bool]:# pragma: no cover
        return None# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
def is_valid_index_factory(leaves: List):# pragma: no cover
    def is_valid_index(idx: int) -> bool:# pragma: no cover
        return 0 <= idx < len(leaves)# pragma: no cover
    return is_valid_index # pragma: no cover
def is_empty_lpar(leaf) -> bool:# pragma: no cover
    return hasattr(leaf, 'empty') and leaf.empty and leaf.type == token.LPAR # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, leaves: List, idx: int) -> int:# pragma: no cover
        return idx + 1 # pragma: no cover
def is_empty_rpar(leaf) -> bool:# pragma: no cover
    return hasattr(leaf, 'empty') and leaf.empty and leaf.type == token.RPAR # pragma: no cover

import token # pragma: no cover

line = type('Mock', (object,), {'leaves': [type('Mock', (object,), {'type': token.NAME, '__str__': lambda self: 'not'})(), type('Mock', (object,), {'type': token.NAME, '__str__': lambda self: ' in'})(), type('Mock', (object,), {'type': token.STRING, '__str__': lambda self: 'mock_string'})()]})() # pragma: no cover
self = type('Mock', (object,), {'_prefer_paren_wrap_match': lambda self, LL: None, 'STRING_OPERATORS': [token.STRING]})() # pragma: no cover
TErr = lambda msg: Exception(msg) # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_empty_lpar = lambda leaf: leaf.type == token.LPAR and str(leaf) == '' # pragma: no cover
StringParser = type('Mock', (object,), {'parse': lambda self, LL, idx: idx + 1}) # pragma: no cover
is_empty_rpar = lambda leaf: leaf.type == token.RPAR and str(leaf) == '' # pragma: no cover
Ok = lambda result: result # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(18620)

if self._prefer_paren_wrap_match(LL) is not None:
    _l_(18622)

    aux = TErr("Line needs to be wrapped in parens first.")
    _l_(18621)
    exit(aux)

is_valid_index = is_valid_index_factory(LL)
_l_(18623)

idx = 0
_l_(18624)

# The first two leaves MAY be the 'not in' keywords...
if (
    is_valid_index(idx)
    and is_valid_index(idx + 1)
    and [LL[idx].type, LL[idx + 1].type] == [token.NAME, token.NAME]
    and str(LL[idx]) + str(LL[idx + 1]) == "not in"
):
    _l_(18628)

    idx += 2
    _l_(18625)
# Else the first leaf MAY be a string operator symbol or the 'in' keyword...
elif is_valid_index(idx) and (
    LL[idx].type in self.STRING_OPERATORS
    or LL[idx].type == token.NAME
    and str(LL[idx]) == "in"
):
    _l_(18627)

    idx += 1
    _l_(18626)

# The next/first leaf MAY be an empty LPAR...
if is_valid_index(idx) and is_empty_lpar(LL[idx]):
    _l_(18630)

    idx += 1
    _l_(18629)

# The next/first leaf MUST be a string...
if not is_valid_index(idx) or LL[idx].type != token.STRING:
    _l_(18632)

    aux = TErr("Line does not start with a string.")
    _l_(18631)
    exit(aux)

string_idx = idx
_l_(18633)

# Skip the string trailer, if one exists.
string_parser = StringParser()
_l_(18634)
idx = string_parser.parse(LL, string_idx)
_l_(18635)

# That string MAY be followed by an empty RPAR...
if is_valid_index(idx) and is_empty_rpar(LL[idx]):
    _l_(18637)

    idx += 1
    _l_(18636)

# That string / empty RPAR leaf MAY be followed by a comma...
if is_valid_index(idx) and LL[idx].type == token.COMMA:
    _l_(18639)

    idx += 1
    _l_(18638)

# But no more leaves are allowed...
if is_valid_index(idx):
    _l_(18641)

    aux = TErr("This line does not end with a string.")
    _l_(18640)
    exit(aux)
aux = Ok([string_idx])
_l_(18642)

exit(aux)
