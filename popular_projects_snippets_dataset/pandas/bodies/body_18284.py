# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
ser = Series(["x", np.nan, "x"])
expected = Series(["xa", np.nan, "xa"])

ser = tm.box_expected(ser, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = ser + "a"
tm.assert_equal(result, expected)
