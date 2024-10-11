import sys # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._warn = lambda: print('Warning') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
self._warn()
_l_(5261)
aux = self.cv.get(None)
_l_(5262)
exit(aux)
