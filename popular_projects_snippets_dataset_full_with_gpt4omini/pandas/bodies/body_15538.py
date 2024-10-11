# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_truncate.py
# GH 35544
series = Series([0.1], index=pd.DatetimeIndex(["2020-08-04"]))
before = pd.Timestamp("2020-08-02")
after = pd.Timestamp("2020-08-04")

result = series.truncate(before=before, after=after)

# the input Series and the expected Series are the same
tm.assert_series_equal(result, series)
