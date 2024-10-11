# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH 23931, 26335
df1 = DataFrame(
    {
        "date": pd.date_range(
            start="2018-01-01", periods=5, tz="America/Chicago"
        ),
        "vals": list("abcde"),
    }
)

df2 = DataFrame(
    {
        "date": pd.date_range(
            start="2018-01-03", periods=5, tz="America/Chicago"
        ),
        "vals_2": list("tuvwx"),
    }
)
result = df1.join(df2.set_index("date"), on="date")
expected = df1.copy()
expected["vals_2"] = Series([np.nan] * 2 + list("tuv"), dtype=object)
tm.assert_frame_equal(result, expected)
