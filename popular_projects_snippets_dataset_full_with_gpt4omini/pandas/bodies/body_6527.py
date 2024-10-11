# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# test the extra keyword
values = [decimal.Decimal("1.1111"), decimal.Decimal("2.2222")]
expected = np.array(
    [decimal.Decimal("1.11"), decimal.Decimal("2.22")], dtype="object"
)
a = pd.array(values, dtype="decimal")
result = a.to_numpy(decimals=2)
tm.assert_numpy_array_equal(result, expected)

result = pd.Series(a).to_numpy(decimals=2)
tm.assert_numpy_array_equal(result, expected)
