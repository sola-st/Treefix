# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
arr = np.array([1, 2, "error"], dtype=object)
result = to_timedelta(arr, unit="ns", errors="ignore")
tm.assert_numpy_array_equal(result, arr)
