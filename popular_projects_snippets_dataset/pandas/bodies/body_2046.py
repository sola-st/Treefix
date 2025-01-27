# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
arr = np.array([1, 2, "error"], dtype=object)
result = to_timedelta(arr, unit="ns", errors="coerce")
expected = to_timedelta([1, 2, pd.NaT], unit="ns")
tm.assert_index_equal(result, expected)
