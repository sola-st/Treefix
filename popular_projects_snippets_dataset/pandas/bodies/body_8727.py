# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
dti = self.index_cls(arr1d)
arr = arr1d

result = getattr(arr, propname)
expected = np.array(getattr(dti, propname), dtype=result.dtype)

tm.assert_numpy_array_equal(result, expected)
