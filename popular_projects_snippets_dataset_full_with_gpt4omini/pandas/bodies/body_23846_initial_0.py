class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.name = 'example' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/pytables.py
from l3.Runtime import _l_
aux = f"{self.name}_dtype"
_l_(5428)
exit(aux)
