# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# https://github.com/pandas-dev/pandas/issues/25077
arr = np.arange(0, 1, 1e-6)[-10:]
result = to_timedelta(arr, unit="s")
expected_asi8 = np.arange(999990000, 10**9, 1000, dtype="int64")
tm.assert_numpy_array_equal(result.asi8, expected_asi8)
