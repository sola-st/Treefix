# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 21603
category_string = Series(list("abc")).astype("category")
df = DataFrame(
    {
        "group": [1, 1, 2],
        "category_string": category_string,
        "datetimetz": pd.date_range("20130101", periods=3, tz="US/Eastern"),
    }
)
result = getattr(df.groupby("group"), method)()
expected = DataFrame(
    {
        "category_string": pd.Categorical(
            [alpha, "c"], dtype=category_string.dtype
        ),
        "datetimetz": [ts, Timestamp("2013-01-03", tz="US/Eastern")],
    },
    index=Index([1, 2], name="group"),
)
tm.assert_frame_equal(result, expected)
