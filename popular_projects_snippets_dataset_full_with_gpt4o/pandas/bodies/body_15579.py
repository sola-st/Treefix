# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#16402
# fillna with a tz aware to a tz-naive, should result in object

ser = Series([Timestamp("20130101"), NaT])

result = ser.fillna(Timestamp("20130101", tz="US/Eastern"))
expected = Series(
    [Timestamp("20130101"), Timestamp("2013-01-01", tz="US/Eastern")],
    dtype="object",
)
tm.assert_series_equal(result, expected)

result = ser.where([True, False], Timestamp("20130101", tz="US/Eastern"))
tm.assert_series_equal(result, expected)

result = ser.where([True, False], Timestamp("20130101", tz="US/Eastern"))
tm.assert_series_equal(result, expected)

# with a non-datetime
result = ser.fillna("foo")
expected = Series([Timestamp("20130101"), "foo"])
tm.assert_series_equal(result, expected)

# assignment
ser2 = ser.copy()
ser2[1] = "foo"
tm.assert_series_equal(ser2, expected)
