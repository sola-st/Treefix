# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
ser = Series(
    [Decimal("1.3"), Decimal("2.3")], index=[date(2012, 1, 1), date(2012, 1, 2)]
)

result = ser + ser.shift(1)
result2 = ser.shift(1) + ser
assert isna(result[0])
assert isna(result2[0])
