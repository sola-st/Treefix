# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_datetime.py
# GH3546 (not including times on the last day)
idx = date_range(start="2013-05-31 00:00", end="2013-05-31 23:00", freq="H")
ts = Series(range(len(idx)), index=idx)
expected = ts["2013-05"]
tm.assert_series_equal(expected, ts)

idx = date_range(start="2013-05-31 00:00", end="2013-05-31 23:59", freq="S")
ts = Series(range(len(idx)), index=idx)
expected = ts["2013-05"]
tm.assert_series_equal(expected, ts)
