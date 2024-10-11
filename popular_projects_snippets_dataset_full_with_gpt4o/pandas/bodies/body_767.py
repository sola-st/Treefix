# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
idx = pd.PeriodIndex(["2011-01", "NaT", "2012-01"], freq="M")
exp = np.array([False, True, False])
tm.assert_numpy_array_equal(isna(idx), exp)
tm.assert_numpy_array_equal(notna(idx), ~exp)

exp = Series([False, True, False])
s = Series(idx)
tm.assert_series_equal(isna(s), exp)
tm.assert_series_equal(notna(s), ~exp)
s = Series(idx, dtype=object)
tm.assert_series_equal(isna(s), exp)
tm.assert_series_equal(notna(s), ~exp)
