import token # pragma: no cover
from typing import List # pragma: no cover
class TErr(Exception): pass # pragma: no cover

class TErr(Exception): pass # pragma: no cover

import token # pragma: no cover
from typing import List # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type_, value):# pragma: no cover
        self.type = type_# pragma: no cover
        self.value = value# pragma: no cover
    def __str__(self):# pragma: no cover
        return self.value # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [# pragma: no cover
            MockLeaf(token.NAME, 'not'),# pragma: no cover
            MockLeaf(token.NAME, 'in'),# pragma: no cover
            MockLeaf(token.STRING, 'example_string'),# pragma: no cover
            MockLeaf(token.COMMA, ',')# pragma: no cover
        ]# pragma: no cover
# pragma: no cover
line = MockLine() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.STRING_OPERATORS = [token.NAME]# pragma: no cover
    def _prefer_paren_wrap_match(self, LL):# pragma: no cover
        return None # pragma: no cover
self = MockSelf() # pragma: no cover
def is_valid_index_factory(LL):# pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_valid_index = is_valid_index_factory(line.leaves) # pragma: no cover
def is_empty_lpar(leaf): return False # pragma: no cover
def is_empty_rpar(leaf): return False # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, LL, idx):# pragma: no cover
        return idx + 1 # pragma: no cover
Ok = lambda value: value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(6897)

if self._prefer_paren_wrap_match(LL) is not None:
    _l_(6899)

    aux = TErr("Line needs to be wrapped in parens first.")
    _l_(6898)
    exit(aux)

is_valid_index = is_valid_index_factory(LL)
_l_(6900)

idx = 0
_l_(6901)

# The first two leaves MAY be the 'not in' keywords...
if (
    is_valid_index(idx)
    and is_valid_index(idx + 1)
    and [LL[idx].type, LL[idx + 1].type] == [token.NAME, token.NAME]
    and str(LL[idx]) + str(LL[idx + 1]) == "not in"
):
    _l_(6905)

    idx += 2
    _l_(6902)
# Else the first leaf MAY be a string operator symbol or the 'in' keyword...
elif is_valid_index(idx) and (
    LL[idx].type in self.STRING_OPERATORS
    or LL[idx].type == token.NAME
    and str(LL[idx]) == "in"
):
    _l_(6904)

    idx += 1
    _l_(6903)

# The next/first leaf MAY be an empty LPAR...
if is_valid_index(idx) and is_empty_lpar(LL[idx]):
    _l_(6907)

    idx += 1
    _l_(6906)

# The next/first leaf MUST be a string...
if not is_valid_index(idx) or LL[idx].type != token.STRING:
    _l_(6909)

    aux = TErr("Line does not start with a string.")
    _l_(6908)
    exit(aux)

string_idx = idx
_l_(6910)

# Skip the string trailer, if one exists.
string_parser = StringParser()
_l_(6911)
idx = string_parser.parse(LL, string_idx)
_l_(6912)

# That string MAY be followed by an empty RPAR...
if is_valid_index(idx) and is_empty_rpar(LL[idx]):
    _l_(6914)

    idx += 1
    _l_(6913)

# That string / empty RPAR leaf MAY be followed by a comma...
if is_valid_index(idx) and LL[idx].type == token.COMMA:
    _l_(6916)

    idx += 1
    _l_(6915)

# But no more leaves are allowed...
if is_valid_index(idx):
    _l_(6918)

    aux = TErr("This line does not end with a string.")
    _l_(6917)
    exit(aux)
aux = Ok([string_idx])
_l_(6919)

exit(aux)
