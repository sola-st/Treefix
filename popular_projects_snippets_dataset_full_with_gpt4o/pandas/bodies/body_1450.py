# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_datetime.py

# GH#8260
# support datetime64 with tz

idx = Index(date_range("20130101", periods=3, tz="US/Eastern"), name="foo")
dr = date_range("20130110", periods=3)
df = DataFrame({"A": idx, "B": dr})
df["C"] = idx
df.iloc[1, 1] = pd.NaT
df.iloc[1, 2] = pd.NaT

expected = Series(
    [Timestamp("2013-01-02 00:00:00-0500", tz="US/Eastern"), pd.NaT, pd.NaT],
    index=list("ABC"),
    dtype="object",
    name=1,
)

# indexing
result = df.iloc[1]
tm.assert_series_equal(result, expected)
result = df.loc[1]
tm.assert_series_equal(result, expected)
