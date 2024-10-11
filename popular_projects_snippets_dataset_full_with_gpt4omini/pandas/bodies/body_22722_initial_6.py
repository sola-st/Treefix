import pandas as pd # pragma: no cover

class MockIndexOpsMixin:  # Mocking the IndexOpsMixin class# pragma: no cover
    def searchsorted(self, value, side='left', sorter=None):# pragma: no cover
        return 0  # Mock behavior for searchsorted # pragma: no cover
base = type('Mock', (object,), {'IndexOpsMixin': MockIndexOpsMixin})() # pragma: no cover
self = base.IndexOpsMixin() # pragma: no cover
value = 3.14 # pragma: no cover
side = 'left' # pragma: no cover
sorter = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/series.py
from l3.Runtime import _l_
aux = base.IndexOpsMixin.searchsorted(self, value, side=side, sorter=sorter)
_l_(10318)
exit(aux)
