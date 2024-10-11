from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self.push = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.push()
_l_(4578)
aux = self
_l_(4579)
exit(aux)
