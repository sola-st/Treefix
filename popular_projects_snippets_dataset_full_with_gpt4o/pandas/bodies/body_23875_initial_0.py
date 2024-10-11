import sys # pragma: no cover

self = type('Mock', (object,), {'nrows': 5})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/pytables.py
from l3.Runtime import _l_
aux = self.nrows
_l_(20876)
exit(aux)
