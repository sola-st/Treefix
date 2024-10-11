import types # pragma: no cover

self = type('Mock', (object,), {'push': lambda self: print('push called')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.push()
_l_(5255)
aux = self
_l_(5256)
exit(aux)
