# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

# from index
idx2 = date_range("20130101", periods=3, tz="US/Eastern", name="foo")
df2 = DataFrame(idx2)
tm.assert_series_equal(df2["foo"], Series(idx2, name="foo"))
df2 = DataFrame(Series(idx2))
tm.assert_series_equal(df2["foo"], Series(idx2, name="foo"))

idx2 = date_range("20130101", periods=3, tz="US/Eastern")
df2 = DataFrame(idx2)
tm.assert_series_equal(df2[0], Series(idx2, name=0))
df2 = DataFrame(Series(idx2))
tm.assert_series_equal(df2[0], Series(idx2, name=0))
