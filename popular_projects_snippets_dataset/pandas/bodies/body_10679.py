# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_shift_diff.py
df = DataFrame({"a": [1, 2, 3, 3, 2], "b": [True, True, False, False, True]})
result = df.groupby("a")["b"].diff()
expected = Series([np.nan, np.nan, np.nan, False, False], name="b")
tm.assert_series_equal(result, expected)
