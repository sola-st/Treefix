import token # pragma: no cover

line = type('Mock', (object,), {'leaves': []}) # pragma: no cover
self = type('Mock', (object,), {'_prefer_paren_wrap_match': lambda self, x: None, 'STRING_OPERATORS': []})() # pragma: no cover
TErr = lambda msg: Exception(msg) # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_empty_lpar = lambda token: False # pragma: no cover
StringParser = type('StringParser', (object,), {'parse': lambda self, LL, idx: idx}) # pragma: no cover
is_empty_rpar = lambda token: False # pragma: no cover
Ok = lambda x: x # pragma: no cover

import token # pragma: no cover

TErr = lambda msg: Exception(msg) # pragma: no cover
Ok = lambda result: result # pragma: no cover
# Token mock class to hold token types # pragma: no cover
class MockToken: # pragma: no cover
    NAME = 1 # pragma: no cover
    STRING = 2 # pragma: no cover
    COMMA = 3 # pragma: no cover
    LPAR = 4 # pragma: no cover
    RPAR = 5 # pragma: no cover
token = MockToken() # pragma: no cover
 # pragma: no cover
# Line mock class with leaves # pragma: no cover
class MockLine: # pragma: no cover
    leaves = [ # pragma: no cover
        type('Token', (object,), {'type': token.STRING, '__str__': lambda self: '"example_string"'})(), # pragma: no cover
        type('Token', (object,), {'type': token.COMMA, '__str__': lambda self: ','})(), # pragma: no cover
        type('Token', (object,), {'type': token.STRING, '__str__': lambda self: '"another_string"'})() # pragma: no cover
    ] # pragma: no cover
line = MockLine() # pragma: no cover
 # pragma: no cover
# Self mock class with required methods and attributes # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.STRING_OPERATORS = [] # pragma: no cover
    def _prefer_paren_wrap_match(self, LL): # pragma: no cover
        return None # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_empty_lpar = lambda leaf: leaf.type == token.LPAR and str(leaf) == '(' # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves, idx): # pragma: no cover
        return idx + 1 # pragma: no cover
is_empty_rpar = lambda leaf: leaf.type == token.RPAR and str(leaf) == ')' # pragma: no cover

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
