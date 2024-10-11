import sys # pragma: no cover

self = type('Mock', (object,), {'msg': 'Exiting the application.'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/debughelpers.py
from l3.Runtime import _l_
aux = self.msg
_l_(6519)
exit(aux)
