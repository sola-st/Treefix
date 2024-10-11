# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
pi = self.index_cls(arr1d)
arr = arr1d

result = getattr(arr, propname)
expected = np.array(getattr(pi, propname))

tm.assert_numpy_array_equal(result, expected)
