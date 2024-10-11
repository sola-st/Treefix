import numpy as np # pragma: no cover
from typing import Any # pragma: no cover

_minmax = lambda func, values, mask, skipna, axis: func(values, axis=axis) # pragma: no cover
values = np.array([1, 2, 3, 4, 5]) # pragma: no cover
mask = np.array([True, True, True, True, True]) # pragma: no cover
skipna = True # pragma: no cover
axis = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
from l3.Runtime import _l_
aux = _minmax(np.min, values=values, mask=mask, skipna=skipna, axis=axis)
_l_(18670)
exit(aux)
