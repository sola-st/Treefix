# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#23524
arr = arr1d
dti = self.index_cls(arr1d)

expected = np.array(list(dti))

result = np.array(arr, dtype=object)
tm.assert_numpy_array_equal(result, expected)

# also test the DatetimeIndex method while we're at it
result = np.array(dti, dtype=object)
tm.assert_numpy_array_equal(result, expected)
