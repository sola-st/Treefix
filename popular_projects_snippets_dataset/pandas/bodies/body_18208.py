# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# resolves issue GH#9787
box = box_with_array
ser = Series([Decimal(10)])
expected = Series([Decimal(5)])

ser = tm.box_expected(ser, box)
expected = tm.box_expected(expected, box)

result = ser / Decimal(2)

tm.assert_equal(result, expected)

result = ser // Decimal(2)
tm.assert_equal(result, expected)
