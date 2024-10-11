import token # pragma: no cover

leaf = type('MockLeaf', (object,), {'type': token.RPAR, 'value': ''})() # pragma: no cover
token = type('MockToken', (object,), {'RPAR': 3}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = leaf.type == token.RPAR and leaf.value == ""
_l_(17094)
exit(aux)
