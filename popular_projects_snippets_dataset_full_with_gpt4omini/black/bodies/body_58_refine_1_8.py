from typing import List, Dict, Any # pragma: no cover

step = 1 # pragma: no cover
class Token:# pragma: no cover
    RPAR = 'RPAR'# pragma: no cover
    RSQB = 'RSQB'# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
    LSQB = 'LSQB'# pragma: no cover
    NAME = 'NAME'# pragma: no cover
    DOT = 'DOT' # pragma: no cover
token = Token() # pragma: no cover
index = 0 # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [# pragma: no cover
            type('MockToken', (object,), {'type': token.NAME, 'value': 'var1'}),# pragma: no cover
            type('MockToken', (object,), {'type': token.DOT, 'value': '.'}),# pragma: no cover
            type('MockToken', (object,), {'type': token.RPAR, 'value': ')'})# pragma: no cover
        ] # pragma: no cover
line = MockLine() # pragma: no cover

from typing import List # pragma: no cover

step = 1 # pragma: no cover
class Token:# pragma: no cover
    RPAR = 'RPAR'# pragma: no cover
    RSQB = 'RSQB'# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
    LSQB = 'LSQB'# pragma: no cover
    NAME = 'NAME'# pragma: no cover
    DOT = 'DOT' # pragma: no cover
token = Token() # pragma: no cover
index = 0 # pragma: no cover
class MockToken:# pragma: no cover
    def __init__(self, token_type, value):# pragma: no cover
        self.type = token_type# pragma: no cover
        self.value = value # pragma: no cover
line = type('MockLine', (object,), { 'leaves': [MockToken(token.NAME, 'var1'), MockToken(token.DOT, '.'), MockToken(token.RPAR, ')'), MockToken(token.NAME, 'for'), MockToken(token.NAME, 'var3')] })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
# Brackets and parentheses indicate calls, subscripts, etc. ...
# basically stuff that doesn't count as "simple". Only a NAME lookup
# or dotted lookup (eg. NAME.NAME) is OK.
from l3.Runtime import _l_
if step == -1:
    _l_(6159)

    disallowed = {token.RPAR, token.RSQB}
    _l_(6157)
else:
    disallowed = {token.LPAR, token.LSQB}
    _l_(6158)

while 0 <= index < len(line.leaves):
    _l_(6166)

    current = line.leaves[index]
    _l_(6160)
    if current.type in disallowed:
        _l_(6162)

        aux = False
        _l_(6161)
        exit(aux)
    if current.type not in {token.NAME, token.DOT} or current.value == "for":
        _l_(6164)

        aux = True
        _l_(6163)
        # If the current token isn't disallowed, we'll assume this is simple as
        # only the disallowed tokens are semantically attached to this lookup
        # expression we're checking. Also, stop early if we hit the 'for' bit
        # of a comprehension.
        exit(aux)

    index += step
    _l_(6165)
aux = True
_l_(6167)

exit(aux)
