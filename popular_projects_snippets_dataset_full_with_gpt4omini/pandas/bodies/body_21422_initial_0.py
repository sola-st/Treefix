import sys # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._freq = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/extension_types.py
from l3.Runtime import _l_
aux = self._freq
_l_(9729)
exit(aux)
