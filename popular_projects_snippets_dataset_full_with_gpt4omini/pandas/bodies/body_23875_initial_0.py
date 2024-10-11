class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.nrows = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/pytables.py
from l3.Runtime import _l_
aux = self.nrows
_l_(10123)
exit(aux)
