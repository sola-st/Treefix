# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
# https://github.com/pandas-dev/pandas/issues/35614
s = pd.Series([{"a", "b", "c"}], index=[1])
result = s.explode().sort_values()
expected = pd.Series(["a", "b", "c"], index=[1, 1, 1])
tm.assert_series_equal(result, expected)
