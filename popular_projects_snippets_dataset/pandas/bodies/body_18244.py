# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
box = box_with_array
ser = Series([1, 2, 3], dtype=dtype)
expected = Series([2, 3, 4], dtype=dtype)

ser = tm.box_expected(ser, box)
expected = tm.box_expected(expected, box)

result = 1 + ser
tm.assert_equal(result, expected)

result = ser + 1
tm.assert_equal(result, expected)
