from pandas.api.extensions import ExtensionDtype # pragma: no cover
import numpy as np # pragma: no cover

class SparseDtype(ExtensionDtype): # pragma: no cover
    def __init__(self, dtype, fill_value=np.nan): # pragma: no cover
        self.dtype = np.dtype(dtype) # pragma: no cover
        self.fill_value = fill_value # pragma: no cover
    def __eq__(self, other): # pragma: no cover
        if not isinstance(other, SparseDtype): # pragma: no cover
            return False # pragma: no cover
        return self.dtype == other.dtype and self.fill_value == other.fill_value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
from l3.Runtime import _l_
dtype = SparseDtype("int", 1)
_l_(19149)
result = SparseDtype(dtype, fill_value=2)
_l_(19150)
expected = SparseDtype("int", 2)
_l_(19151)
assert result == expected
_l_(19152)
