# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#4532
# operate with pd.offsets
ser = Series([Timestamp("20130101 9:01"), Timestamp("20130101 9:02")])
expected = Series(
    [Timestamp("20130101 9:00:55"), Timestamp("20130101 9:01:55")]
)

ser = tm.box_expected(ser, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = ser - pd.offsets.Second(5)
tm.assert_equal(result, expected)

result2 = -pd.offsets.Second(5) + ser
tm.assert_equal(result2, expected)
msg = "(bad|unsupported) operand type for unary"
with pytest.raises(TypeError, match=msg):
    pd.offsets.Second(5) - ser
