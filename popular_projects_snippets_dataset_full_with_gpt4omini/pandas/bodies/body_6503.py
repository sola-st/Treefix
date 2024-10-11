# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
arr = DecimalArray([decimal.Decimal("10.0")])
result = pd.Series(arr, dtype=DecimalDtype())
expected = pd.Series(arr)
tm.assert_series_equal(result, expected)

result = pd.Series(arr, dtype="int64")
expected = pd.Series([10])
tm.assert_series_equal(result, expected)
