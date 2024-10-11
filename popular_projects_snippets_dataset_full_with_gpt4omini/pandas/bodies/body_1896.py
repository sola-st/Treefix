# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH3609
s = Series(
    range(100),
    index=date_range("20130101", freq="s", periods=100, name="idx"),
    dtype="float",
)
s[10:30] = np.nan
index = PeriodIndex(
    [Period("2013-01-01 00:00", "T"), Period("2013-01-01 00:01", "T")],
    name="idx",
)
expected = Series([34.5, 79.5], index=index)
result = s.to_period().resample("T", kind="period").mean()
tm.assert_series_equal(result, expected)
result2 = s.resample("T", kind="period").mean()
tm.assert_series_equal(result2, expected)
