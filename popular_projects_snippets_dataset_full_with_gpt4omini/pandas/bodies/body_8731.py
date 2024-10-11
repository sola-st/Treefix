# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d

result = arr.strftime("%Y %b")
expected = np.array([ts.strftime("%Y %b") for ts in arr], dtype=object)
tm.assert_numpy_array_equal(result, expected)
