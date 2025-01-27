# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
df = DataFrame(
    {"a": [1, 2, 3] * 2, "dates": date_range("now", periods=6, freq="T")}
)
result = df.groupby("a").dates.count()
expected = Series([2, 2, 2], index=Index([1, 2, 3], name="a"), name="dates")
tm.assert_series_equal(result, expected)
