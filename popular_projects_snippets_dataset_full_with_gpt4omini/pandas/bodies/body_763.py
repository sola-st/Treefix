# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
idx = DatetimeIndex(["2011-01-01", "NaT", "2011-01-02"])
exp = np.array([False, True, False])
tm.assert_numpy_array_equal(isna(idx), exp)
tm.assert_numpy_array_equal(notna(idx), ~exp)
tm.assert_numpy_array_equal(isna(idx.values), exp)
tm.assert_numpy_array_equal(notna(idx.values), ~exp)
