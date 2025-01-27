# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
idx = TimedeltaIndex(["1 days", "NaT", "2 days"])
exp = np.array([False, True, False])
tm.assert_numpy_array_equal(isna(idx), exp)
tm.assert_numpy_array_equal(notna(idx), ~exp)
tm.assert_numpy_array_equal(isna(idx.values), exp)
tm.assert_numpy_array_equal(notna(idx.values), ~exp)
