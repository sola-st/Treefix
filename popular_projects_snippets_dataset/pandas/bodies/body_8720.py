# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
dti = self.index_cls(arr1d)

expected = dti.asi8
result = np.array(arr, dtype="i8")
tm.assert_numpy_array_equal(result, expected)

result = np.array(arr, dtype=np.int64)
tm.assert_numpy_array_equal(result, expected)

# check that we are still making copies when setting copy=False
result = np.array(arr, dtype="i8", copy=False)
assert result.base is not expected.base
assert result.base is None
