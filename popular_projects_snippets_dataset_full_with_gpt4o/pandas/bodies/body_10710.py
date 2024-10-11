# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
s = Series([1.0, 2.0, np.nan, 3.0])
grouped = s.groupby([0, 1, 2, 2])

result = grouped.agg(builtins.sum)
result2 = grouped.apply(builtins.sum)
expected = grouped.sum()
tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)
