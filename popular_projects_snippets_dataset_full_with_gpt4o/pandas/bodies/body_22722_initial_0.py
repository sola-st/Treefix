import numpy as np # pragma: no cover

base = type('MockBase', (object,), {'IndexOpsMixin': type('MockIndexOpsMixin', (object,), {'searchsorted': lambda self, value, side, sorter: np.searchsorted([1, 2, 3, 4, 5], value, side=side, sorter=sorter)})}) # pragma: no cover
self = base.IndexOpsMixin() # pragma: no cover
value = 3 # pragma: no cover
side = 'left' # pragma: no cover
sorter = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/series.py
from l3.Runtime import _l_
aux = base.IndexOpsMixin.searchsorted(self, value, side=side, sorter=sorter)
_l_(21375)
exit(aux)
