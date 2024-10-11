# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
s = Series(period_range("1/1/2000", periods=10), dtype=PeriodDtype("D"))
exp = Series(period_range("1/1/2000", periods=10))
tm.assert_series_equal(s, exp)
