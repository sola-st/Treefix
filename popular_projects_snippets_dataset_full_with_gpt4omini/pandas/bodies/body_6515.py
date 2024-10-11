# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# op(EA, EA) should return an EA, or an ndarray if it's not possible
# to return an EA with the return values.
arr = class_([decimal.Decimal("1.0"), decimal.Decimal("2.0")])
result = arr + arr
expected = np.array(
    [decimal.Decimal("2.0"), decimal.Decimal("4.0")], dtype="object"
)
tm.assert_numpy_array_equal(result, expected)
