import sys # pragma: no cover

token = type("Mock", (object,), {"NUMBER": 0}) # pragma: no cover
nl = type("Mock", (object,), {"type": token.NUMBER})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
aux = nl.type == token.NUMBER
_l_(20095)
exit(aux)
