# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# check _HANDLED_TYPES
a = to_decimal([1, 2, 3])
s = pd.Series(a)
result = np.add(s, decimal.Decimal(1))
expected = pd.Series(np.add(a, decimal.Decimal(1)))
tm.assert_series_equal(result, expected)
