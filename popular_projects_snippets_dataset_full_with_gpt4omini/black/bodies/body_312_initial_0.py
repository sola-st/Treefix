from unittest.mock import Mock # pragma: no cover

nl = Mock() # pragma: no cover
nl.type = 'LPAR' # pragma: no cover
token = Mock() # pragma: no cover
token.LPAR = 'LPAR' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = nl.type == token.LPAR
_l_(6287)
exit(aux)
