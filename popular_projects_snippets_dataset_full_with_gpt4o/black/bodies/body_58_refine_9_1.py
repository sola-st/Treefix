import token # pragma: no cover

step = 1 # pragma: no cover
index = 0 # pragma: no cover
line = type("Mock", (object,), {"leaves": [type("Mock", (object,), {"type": token.NAME, "value": "example"})()]})() # pragma: no cover

import token # pragma: no cover

step = 1 # pragma: no cover
index = 0 # pragma: no cover
token = type('MockToken', (object,), {'RPAR': 1, 'RSQB': 2, 'LPAR': 3, 'LSQB': 4, 'NAME': 5, 'DOT': 6})() # pragma: no cover
line = type('MockLine', (object,), {'leaves': [type('MockLeaf', (object,), {'type': token.NAME, 'value': 'example'})(), type('MockLeaf', (object,), {'type': token.DOT, 'value': '.'})(), type('MockLeaf', (object,), {'type': token.NAME, 'value': 'for'})(), type('MockLeaf', (object,), {'type': token.RPAR, 'value': ')'})()]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
# Brackets and parentheses indicate calls, subscripts, etc. ...
# basically stuff that doesn't count as "simple". Only a NAME lookup
# or dotted lookup (eg. NAME.NAME) is OK.
from l3.Runtime import _l_
if step == -1:
    _l_(17849)

    disallowed = {token.RPAR, token.RSQB}
    _l_(17847)
else:
    disallowed = {token.LPAR, token.LSQB}
    _l_(17848)

while 0 <= index < len(line.leaves):
    _l_(17856)

    current = line.leaves[index]
    _l_(17850)
    if current.type in disallowed:
        _l_(17852)

        aux = False
        _l_(17851)
        exit(aux)
    if current.type not in {token.NAME, token.DOT} or current.value == "for":
        _l_(17854)

        aux = True
        _l_(17853)
        # If the current token isn't disallowed, we'll assume this is simple as
        # only the disallowed tokens are semantically attached to this lookup
        # expression we're checking. Also, stop early if we hit the 'for' bit
        # of a comprehension.
        exit(aux)

    index += step
    _l_(17855)
aux = True
_l_(17857)

exit(aux)
