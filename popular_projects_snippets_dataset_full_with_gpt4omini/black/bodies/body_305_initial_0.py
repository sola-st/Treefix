from unittest.mock import Mock # pragma: no cover

token = type('MockToken', (), {'RPAR': 'RPAR'})() # pragma: no cover
leaf = Mock() # pragma: no cover
leaf.type = token.RPAR # pragma: no cover
leaf.value = '' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = leaf.type == token.RPAR and leaf.value == ""
_l_(5462)
exit(aux)
