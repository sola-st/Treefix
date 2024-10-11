# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
a = to_decimal([1, 2, 3])
s = pd.Series(a)
result = np.exp(s)
expected = pd.Series(to_decimal(np.exp(a._data)))
tm.assert_series_equal(result, expected)
