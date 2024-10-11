# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 13467
exp = Series([np.nan, np.nan], dtype=np.float64)
assert exp.dtype == np.float64
tm.assert_series_equal(Series([np.nan, np.nan]), exp)
tm.assert_series_equal(Series(np.array([np.nan, np.nan])), exp)

exp = Series([NaT, NaT])
assert exp.dtype == "datetime64[ns]"
tm.assert_series_equal(Series([NaT, NaT]), exp)
tm.assert_series_equal(Series(np.array([NaT, NaT])), exp)

tm.assert_series_equal(Series([NaT, np.nan]), exp)
tm.assert_series_equal(Series(np.array([NaT, np.nan])), exp)

tm.assert_series_equal(Series([np.nan, NaT]), exp)
tm.assert_series_equal(Series(np.array([np.nan, NaT])), exp)
