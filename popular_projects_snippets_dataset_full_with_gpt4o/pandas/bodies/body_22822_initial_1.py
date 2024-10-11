import numpy as np # pragma: no cover

_minmax = np.fmin # pragma: no cover
values = np.array([3, 5, 1, 7]) # pragma: no cover
mask = np.array([True, True, False, True]) # pragma: no cover
skipna = True # pragma: no cover
axis = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
from l3.Runtime import _l_
aux = _minmax(np.min, values=values, mask=mask, skipna=skipna, axis=axis)
_l_(18670)
exit(aux)
