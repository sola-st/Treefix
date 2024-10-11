# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
# GH 10114
df = DataFrame(
    {
        "A": np.arange(5, dtype="int64"),
        "B": ["foo", "bar", "foo", "bar", "bar"],
        "C": Timestamp("20130101"),
    }
)

grouped = df.groupby(["B", "C"])

result = grouped["A"].filter(lambda x: True)
tm.assert_series_equal(df["A"], result)

result = grouped["A"].transform(len)
expected = Series([2, 3, 2, 3, 3], name="A")
tm.assert_series_equal(result, expected)

result = grouped.filter(lambda x: True)
tm.assert_frame_equal(df, result)

result = grouped.transform("sum")
expected = DataFrame({"A": [2, 8, 2, 8, 8]})
tm.assert_frame_equal(result, expected)

result = grouped.transform(len)
expected = DataFrame({"A": [2, 3, 2, 3, 3]})
tm.assert_frame_equal(result, expected)
