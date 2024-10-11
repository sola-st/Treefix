import numpy as np # pragma: no cover
from pandas._libs import lib # pragma: no cover
import pandas._testing as tm # pragma: no cover

value = 123 # pragma: no cover
lib = type('Mock', (object,), {'maybe_convert_objects': lambda arr: arr}) # pragma: no cover
tm = type('Mock', (object,), {'assert_numpy_array_equal': lambda a, b: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# see gh-18584
from l3.Runtime import _l_
arr = np.array([value], dtype=object)
_l_(21986)
result = lib.maybe_convert_objects(arr)
_l_(21987)
tm.assert_numpy_array_equal(arr, result)
_l_(21988)
