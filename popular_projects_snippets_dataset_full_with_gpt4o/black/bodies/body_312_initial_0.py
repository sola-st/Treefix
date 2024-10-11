import token # pragma: no cover

nl = type('Mock', (object,), {'type': token.LPAR}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = nl.type == token.LPAR
_l_(18066)
exit(aux)
