import numpy as np # pragma: no cover
from typing import Optional, Any # pragma: no cover

_minmax = lambda func, values, mask, skipna, axis: func(np.ma.masked_array(values, mask=mask), axis=axis) if skipna else func(values, axis=axis) # pragma: no cover
values = [1, 2, 3, 4, 5] # pragma: no cover
mask = [False, False, True, False, False] # pragma: no cover
skipna = True # pragma: no cover
axis = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
from l3.Runtime import _l_
aux = _minmax(np.min, values=values, mask=mask, skipna=skipna, axis=axis)
_l_(6727)
exit(aux)
