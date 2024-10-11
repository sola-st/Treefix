import numpy as np # pragma: no cover

nv = type('Mock', (object,), {'validate_min': lambda self, a, b: None})() # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover
masked_reductions = type('Mock', (object,), {'min': lambda data, mask, skipna, axis: np.min(data)})() # pragma: no cover
self = type('Mock', (object,), {'_data': np.array([1, 2, 3, 4, 5]), '_mask': np.array([False, False, False, False, False])})() # pragma: no cover
skipna = True # pragma: no cover
axis = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
from l3.Runtime import _l_
nv.validate_min((), kwargs)
_l_(21809)
aux = masked_reductions.min(
    self._data,
    self._mask,
    skipna=skipna,
    axis=axis,
)
_l_(21810)
exit(aux)
