# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
a = data[:5]
s = pd.Series(a, index=range(3, 8))
result = np.abs(s)
expected = pd.Series(np.abs(a), index=range(3, 8))
tm.assert_series_equal(result, expected)
