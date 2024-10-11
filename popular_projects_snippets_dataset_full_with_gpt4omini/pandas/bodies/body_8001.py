# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
xp = period_range("2012-1-1", freq="M", periods=3)
rs = Index(xp)
tm.assert_index_equal(rs, xp)
assert isinstance(rs, PeriodIndex)
