# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#4532
# operate with pd.offsets
ser = Series([Timestamp("20130101 9:01"), Timestamp("20130101 9:02")])
expected = Series(
    [Timestamp("20130101 9:01:05"), Timestamp("20130101 9:02:05")]
)

ser = tm.box_expected(ser, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = ser + pd.offsets.Second(5)
tm.assert_equal(result, expected)

result2 = pd.offsets.Second(5) + ser
tm.assert_equal(result2, expected)
