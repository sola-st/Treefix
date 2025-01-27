# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# Test for #30050
ser = Series([1, 2, None, 2**61, None])
ser = ser.astype("Int64")
ser_copy = ser.copy()

res = to_datetime(ser, unit="ns")

expected = Series(
    [
        np.datetime64("1970-01-01 00:00:00.000000001"),
        np.datetime64("1970-01-01 00:00:00.000000002"),
        np.datetime64("NaT"),
        np.datetime64("2043-01-25 23:56:49.213693952"),
        np.datetime64("NaT"),
    ]
)
tm.assert_series_equal(res, expected)
# Check that ser isn't mutated
tm.assert_series_equal(ser, ser_copy)
