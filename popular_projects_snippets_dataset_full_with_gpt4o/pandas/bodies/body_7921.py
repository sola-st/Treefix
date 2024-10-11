# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
rng = period_range(start="2012-01-01", periods=10, freq="W-MON")
ts = Series(range(len(rng)), index=rng)

dt1 = datetime(2011, 10, 2)
dt4 = datetime(2012, 4, 20)

rs = ts[dt1:dt4]
tm.assert_series_equal(rs, ts)
