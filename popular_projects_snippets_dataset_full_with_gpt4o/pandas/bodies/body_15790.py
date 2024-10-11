# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#9757
ts = Series([Timestamp("2010-01-04 00:00:00")])
res = ts.astype(str)

expected = Series(["2010-01-04"])
tm.assert_series_equal(res, expected)

ts = Series([Timestamp("2010-01-04 00:00:00", tz="US/Eastern")])
res = ts.astype(str)

expected = Series(["2010-01-04 00:00:00-05:00"])
tm.assert_series_equal(res, expected)
