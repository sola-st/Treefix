# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# arrays of various dtypes
arr = np.array([1] * 5, dtype=dtype)
result = to_timedelta(arr, unit=unit)
exp_dtype = "m8[ns]" if dtype == "int64" else "m8[s]"
expected = TimedeltaIndex([np.timedelta64(1, unit)] * 5, dtype=exp_dtype)
tm.assert_index_equal(result, expected)
