# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# 2d slicing on a 1D array
expected = type(arr1d)(arr1d._ndarray[:, np.newaxis], dtype=arr1d.dtype)
result = arr1d[:, np.newaxis]
tm.assert_equal(result, expected)

# Lookup on a 2D array
arr2d = expected
expected = type(arr2d)(arr2d._ndarray[:3, 0], dtype=arr2d.dtype)
result = arr2d[:3, 0]
tm.assert_equal(result, expected)

# Scalar lookup
result = arr2d[-1, 0]
expected = arr1d[-1]
assert result == expected
