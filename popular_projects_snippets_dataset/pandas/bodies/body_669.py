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
