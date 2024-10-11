from typing import Callable # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._validate_index_level = lambda level: None # pragma: no cover
level = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
from l3.Runtime import _l_
self._validate_index_level(level)
_l_(10175)
aux = 0
_l_(10176)
exit(aux)
