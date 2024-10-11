# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d

result = arr.strftime("%Y")
expected = np.array([per.strftime("%Y") for per in arr], dtype=object)
tm.assert_numpy_array_equal(result, expected)
