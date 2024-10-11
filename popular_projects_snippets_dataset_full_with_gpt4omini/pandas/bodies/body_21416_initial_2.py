import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

class MockNV:# pragma: no cover
    def validate_min(self, arg1, arg2):# pragma: no cover
        return True# pragma: no cover
nv = MockNV() # pragma: no cover
kwargs = {'arg1': 1, 'arg2': 2} # pragma: no cover
class MockMaskedReductions:# pragma: no cover
    @staticmethod# pragma: no cover
    def min(data, mask, skipna, axis):# pragma: no cover
        return np.nanmin(data[mask]) if skipna else np.min(data[mask])# pragma: no cover
masked_reductions = MockMaskedReductions() # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._data = np.array([1, 2, 3, 4, 5])# pragma: no cover
        self._mask = np.array([True, True, False, True, True])# pragma: no cover
self = MockSelf() # pragma: no cover
skipna = True # pragma: no cover
axis = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
from l3.Runtime import _l_
nv.validate_min((), kwargs)
_l_(10555)
aux = masked_reductions.min(
    self._data,
    self._mask,
    skipna=skipna,
    axis=axis,
)
_l_(10556)
exit(aux)
