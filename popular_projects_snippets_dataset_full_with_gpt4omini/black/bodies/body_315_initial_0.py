from unittest.mock import Mock # pragma: no cover

token = Mock(NUMBER='number') # pragma: no cover
nl = Mock(type=token.NUMBER) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = nl.type == token.NUMBER
_l_(8599)
exit(aux)
