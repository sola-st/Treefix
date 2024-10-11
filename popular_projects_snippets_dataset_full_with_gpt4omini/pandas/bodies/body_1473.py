# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# GH4726
# dup indexing with iloc/loc
df = DataFrame(
    [[1, 2, "foo", "bar", Timestamp("20130101")]],
    columns=["a", "a", "a", "a", "a"],
    index=[1],
)
expected = Series(
    [1, 2, "foo", "bar", Timestamp("20130101")],
    index=["a", "a", "a", "a", "a"],
    name=1,
)

result = df.iloc[0]
tm.assert_series_equal(result, expected)

result = df.loc[1]
tm.assert_series_equal(result, expected)
