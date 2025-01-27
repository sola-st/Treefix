# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
arr = DecimalArray([decimal.Decimal("10.0")])

result = pd.DataFrame({"A": arr}, dtype=DecimalDtype())
expected = pd.DataFrame({"A": arr})
tm.assert_frame_equal(result, expected)

arr = DecimalArray([decimal.Decimal("10.0")])
result = pd.DataFrame({"A": arr}, dtype="int64")
expected = pd.DataFrame({"A": [10]})
tm.assert_frame_equal(result, expected)
