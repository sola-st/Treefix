class Mock(object): # pragma: no cover
    def _validate_index_level(self, level): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
level = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
from l3.Runtime import _l_
self._validate_index_level(level)
_l_(20900)
aux = 0
_l_(20901)
exit(aux)
