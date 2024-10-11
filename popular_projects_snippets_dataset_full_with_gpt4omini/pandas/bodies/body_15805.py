# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH37553
ser = Series([4, 0, 9], dtype=dtype)
result = ser.astype(DatetimeTZDtype(tz="US/Pacific"))

expected = Series(
    {
        0: Timestamp("1969-12-31 16:00:00.000000004-08:00", tz="US/Pacific"),
        1: Timestamp("1969-12-31 16:00:00.000000000-08:00", tz="US/Pacific"),
        2: Timestamp("1969-12-31 16:00:00.000000009-08:00", tz="US/Pacific"),
    }
)

tm.assert_series_equal(result, expected)
