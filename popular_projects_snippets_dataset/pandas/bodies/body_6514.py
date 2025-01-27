# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# https://github.com/pandas-dev/pandas/issues/22850
cls = DecimalArrayWithoutFromSequence

@classmethod
def construct_array_type(cls):
    exit(DecimalArrayWithoutFromSequence)

monkeypatch.setattr(DecimalDtype, "construct_array_type", construct_array_type)

arr = cls([decimal.Decimal("1.0"), decimal.Decimal("2.0")])
ser = pd.Series(arr)
result = ser.combine(ser, operator.add)

# note: object dtype
expected = pd.Series(
    [decimal.Decimal("2.0"), decimal.Decimal("4.0")], dtype="object"
)
tm.assert_series_equal(result, expected)
