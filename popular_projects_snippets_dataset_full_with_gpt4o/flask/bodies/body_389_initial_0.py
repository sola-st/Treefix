from threading import Condition # pragma: no cover

self = type('Mock', (object,), {'_warn': lambda self: print('Warning!'), 'cv': Condition()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
self._warn()
_l_(22579)
aux = self.cv.get(None)
_l_(22580)
exit(aux)
