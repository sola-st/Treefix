# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH 12981
# Assignment of unaligned offset-aware datetime series.
# Make sure timezone isn't lost
column = Series(date_range("2015-01-01", periods=3, tz="utc"), name="dates")
df = DataFrame({"dates": column})
df["dates"] = column[[1, 0, 2]]
tm.assert_series_equal(df["dates"], column)

df = DataFrame({"dates": column})
df.loc[[0, 1, 2], "dates"] = column[[1, 0, 2]]
tm.assert_series_equal(df["dates"], column)
