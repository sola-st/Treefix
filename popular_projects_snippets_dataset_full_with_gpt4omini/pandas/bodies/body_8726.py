# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# in this case _bool_ops is just `is_leap_year`
dti = self.index_cls(arr1d)
arr = arr1d
assert dti.freq == arr.freq

result = getattr(arr, propname)
expected = np.array(getattr(dti, propname), dtype=result.dtype)

tm.assert_numpy_array_equal(result, expected)
