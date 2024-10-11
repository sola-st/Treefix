# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
df = DataFrame({"a": [1, 2, 2], "b": data})
result = df.groupby("a")["b"].diff()
expected = Series([NaT, NaT, Timedelta("1 days")], name="b")
tm.assert_series_equal(result, expected)
