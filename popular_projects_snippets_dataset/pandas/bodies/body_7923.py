# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH 7710
rng = period_range(start="2012-01-01", periods=10, freq="D")
ts = Series(range(len(rng)), index=rng)
exp = ts.iloc[[1]]
tm.assert_series_equal(ts[[Period("2012-01-02", freq="D")]], exp)
