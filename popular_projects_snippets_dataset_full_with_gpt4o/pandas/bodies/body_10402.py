# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 13191
df = DataFrame(
    {"grouping": [np.nan, 1, 1, 3], "d": date_range("2014-1-1", "2014-1-4")}
)
result = df.groupby("grouping")["d"].transform("first")
dates = [
    pd.NaT,
    Timestamp("2014-1-2"),
    Timestamp("2014-1-2"),
    Timestamp("2014-1-4"),
]
expected = Series(dates, name="d")
tm.assert_series_equal(result, expected)
