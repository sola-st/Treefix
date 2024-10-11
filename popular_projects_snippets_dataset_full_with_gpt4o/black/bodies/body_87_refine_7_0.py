from typing import List, Any # pragma: no cover

class MockLine: # pragma: no cover
    def __init__(self, leaves: List[Any]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, string_operators: List[int]): # pragma: no cover
        self.STRING_OPERATORS = string_operators # pragma: no cover
     # pragma: no cover
    def _prefer_paren_wrap_match(self, leaves: List[Any]) -> Any: # pragma: no cover
        # Mock implementation, always returns None # pragma: no cover
        return None # pragma: no cover
 # pragma: no cover
class MockToken: # pragma: no cover
    NAME = 1 # pragma: no cover
    STRING = 2 # pragma: no cover
    COMMA = 3 # pragma: no cover
 # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves: List[Any], string_idx: int) -> int: # pragma: no cover
        # Mock implementation # pragma: no cover
        return string_idx + 1 # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Any]): # pragma: no cover
    def is_valid_index(idx: int) -> bool: # pragma: no cover
        return 0 <= idx < len(leaves) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_empty_lpar(leaf: Any) -> bool: # pragma: no cover
    # Mock implementation, always returns False # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
def is_empty_rpar(leaf: Any) -> bool: # pragma: no cover
    # Mock implementation, always returns False # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def TErr(message: str) -> str: # pragma: no cover
    return message # pragma: no cover
 # pragma: no cover
def Ok(value: Any) -> str: # pragma: no cover
    return 'Ok' # pragma: no cover
 # pragma: no cover
# Initializing variables with mock values # pragma: no cover
line = MockLine(leaves=[]) # pragma: no cover
self = MockSelf(string_operators=[1, 2, 3]) # pragma: no cover
token = MockToken() # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class MockLine: # pragma: no cover
    def __init__(self, leaves: List[Any]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, string_operators: List[int]): # pragma: no cover
        self.STRING_OPERATORS = string_operators # pragma: no cover
     # pragma: no cover
    def _prefer_paren_wrap_match(self, leaves: List[Any]) -> Any: # pragma: no cover
        # Mock implementation, always returns None # pragma: no cover
        return None # pragma: no cover
 # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves: List[Any], string_idx: int) -> int: # pragma: no cover
        # Mock implementation # pragma: no cover
        return string_idx + 1 # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Any]): # pragma: no cover
    def is_valid_index(idx: int) -> bool: # pragma: no cover
        return 0 <= idx < len(leaves) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_empty_lpar(leaf: Any) -> bool: # pragma: no cover
    # Mock implementation, always returns False # pragma: no cover
    return leaf.type == token.LPAR and str(leaf) == '(' # pragma: no cover
 # pragma: no cover
def is_empty_rpar(leaf: Any) -> bool: # pragma: no cover
    # Mock implementation, always returns False # pragma: no cover
    return leaf.type == token.RPAR and str(leaf) == ')' # pragma: no cover
 # pragma: no cover
def TErr(message: str) -> str: # pragma: no cover
    return message # pragma: no cover
 # pragma: no cover
def Ok(value: Any) -> str: # pragma: no cover
    return 'Ok: {value}' # pragma: no cover
 # pragma: no cover
# Initializing variables with mock values # pragma: no cover
line = MockLine(leaves=[ # pragma: no cover
    type('Mock', (object,), {'type': token.NAME, '__str__': lambda self: 'not'})(), # pragma: no cover
    type('Mock', (object,), {'type': token.NAME, '__str__': lambda self: 'in'})(), # pragma: no cover
    type('Mock', (object,), {'type': token.STRING, '__str__': lambda self: '"example"'})() # pragma: no cover
]) # pragma: no cover
self = MockSelf(string_operators=[token.STRING]) # pragma: no cover

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
