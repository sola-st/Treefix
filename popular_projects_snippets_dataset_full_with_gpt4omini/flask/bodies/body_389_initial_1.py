import sys # pragma: no cover
import unittest.mock # pragma: no cover

self = type('MockSelf', (), {'_warn': unittest.mock.Mock(), 'cv': type('MockCV', (), {'get': lambda self, x: 1})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/globals.py
from l3.Runtime import _l_
self._warn()
_l_(5261)
aux = self.cv.get(None)
_l_(5262)
exit(aux)
