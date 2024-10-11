self = type('Mock', (object,), {'push': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.push()
_l_(16258)
aux = self
_l_(16259)
exit(aux)
