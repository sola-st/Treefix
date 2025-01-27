# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
arr = DecimalArray([decimal.Decimal("1.0"), decimal.Decimal("2.0")])
result = arr.take([0, -1], allow_fill=True, fill_value=decimal.Decimal("-1.0"))
expected = DecimalArray([decimal.Decimal("1.0"), decimal.Decimal("-1.0")])
self.assert_extension_array_equal(result, expected)
