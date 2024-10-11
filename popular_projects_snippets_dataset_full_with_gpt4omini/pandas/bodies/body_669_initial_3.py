import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pytest # pragma: no cover

value = pd.Series([1, 2, 3]) # pragma: no cover
lib = type('Mock', (object,), {'maybe_convert_objects': lambda arr: arr})() # pragma: no cover
tm = type('Mock', (object,), {'assert_numpy_array_equal': lambda arr1, arr2: np.array_equal(arr1, arr2)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# see gh-18584
from l3.Runtime import _l_
arr = np.array([value], dtype=object)
_l_(10605)
result = lib.maybe_convert_objects(arr)
_l_(10606)
tm.assert_numpy_array_equal(arr, result)
_l_(10607)
