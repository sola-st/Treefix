from typing import List, Dict, Any # pragma: no cover
import enum # pragma: no cover

class Token(enum.Enum): # pragma: no cover
    RPAR = ')' # pragma: no cover
    RSQB = ']' # pragma: no cover
    LPAR = '(' # pragma: no cover
    LSQB = '[' # pragma: no cover
    NAME = 'name' # pragma: no cover
    DOT = '.' # pragma: no cover
token = Token # pragma: no cover
step = 1 # pragma: no cover
index = 0 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves: List[Any]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
line = Line(leaves=[{'type': 'name', 'value': 'abc'}, {'type': 'name', 'value': 'for'}, {'type': 'name', 'value': 'def'}]) # pragma: no cover

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
