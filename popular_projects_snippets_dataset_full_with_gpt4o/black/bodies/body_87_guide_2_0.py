import token # pragma: no cover

class TErr(Exception): # pragma: no cover
    def __init__(self, message): # pragma: no cover
        self.message = message # pragma: no cover
    def __str__(self): # pragma: no cover
        return self.message # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves): # pragma: no cover
    def is_valid_index(idx): # pragma: no cover
        return 0 <= idx < len(leaves) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_empty_lpar(leaf): # pragma: no cover
    return leaf.type == token.LPAR and leaf.value == '(' # pragma: no cover
 # pragma: no cover
def is_empty_rpar(leaf): # pragma: no cover
    return leaf.type == token.RPAR and leaf.value == ')' # pragma: no cover
 # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves, idx): # pragma: no cover
        return idx + 1 # pragma: no cover
 # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
    def __str__(self): # pragma: no cover
        return self.value # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    STRING_OPERATORS = {token.STAR, token.PLUS, token.STRING} # pragma: no cover
    def _prefer_paren_wrap_match(self, LL): # pragma: no cover
        return 'mock_value'  # Return a non-None value to trigger the uncovered path # pragma: no cover
 # pragma: no cover
line = type('Line', (object,), {'leaves': [ # pragma: no cover
    MockLeaf(token.NAME, 'not'), # pragma: no cover
    MockLeaf(token.NAME, ' in'), # pragma: no cover
    MockLeaf(token.LPAR, '('), # pragma: no cover
    MockLeaf(token.STRING, '"example_string"'), # pragma: no cover
    MockLeaf(token.RPAR, ')'), # pragma: no cover
    MockLeaf(token.COMMA, ','), # pragma: no cover
]})() # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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
