# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH7932
# converting a PeriodIndex when put in a Series

pi = period_range("20130101", periods=5, freq="D")
s = Series(pi)
assert s.dtype == "Period[D]"
expected = Series(pi.astype(object))
tm.assert_series_equal(s, expected)
