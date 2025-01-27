# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# in this case _bool_ops is just `is_leap_year`
pi = self.index_cls(arr1d)
arr = arr1d

result = getattr(arr, propname)
expected = np.array(getattr(pi, propname))

tm.assert_numpy_array_equal(result, expected)
