# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
ser = Series(["x", np.nan, "x"])
expected = Series(["ax", np.nan, "ax"])

ser = tm.box_expected(ser, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = "a" + ser
tm.assert_equal(result, expected)
