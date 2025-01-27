# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#23524
arr = arr1d
dti = self.index_cls(arr1d)

expected = dti.asi8.view("M8[ns]")
result = np.array(arr, dtype="M8[ns]")
tm.assert_numpy_array_equal(result, expected)

result = np.array(arr, dtype="datetime64[ns]")
tm.assert_numpy_array_equal(result, expected)

# check that we are not making copies when setting copy=False
result = np.array(arr, dtype="M8[ns]", copy=False)
assert result.base is expected.base
assert result.base is not None
result = np.array(arr, dtype="datetime64[ns]", copy=False)
assert result.base is expected.base
assert result.base is not None
