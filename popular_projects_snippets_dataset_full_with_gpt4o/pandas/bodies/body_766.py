# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
idx = TimedeltaIndex(["1 days", "NaT", "2 days"])
values = idx.values.astype(dtype)

exp = np.array([False, True, False])
tm.assert_numpy_array_equal(isna(values), exp)
tm.assert_numpy_array_equal(notna(values), ~exp)

exp = Series([False, True, False])
s = Series(values)
tm.assert_series_equal(isna(s), exp)
tm.assert_series_equal(notna(s), ~exp)
s = Series(values, dtype=object)
tm.assert_series_equal(isna(s), exp)
tm.assert_series_equal(notna(s), ~exp)
