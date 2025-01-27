# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# with timezone
# GH#15855
ser = Series([Timestamp("2012-11-11 00:00:00+01:00"), NaT])
exp = Series(
    [
        Timestamp("2012-11-11 00:00:00+01:00"),
        Timestamp("2012-11-11 00:00:00+01:00"),
    ]
)
tm.assert_series_equal(ser.fillna(method="pad"), exp)

ser = Series([NaT, Timestamp("2012-11-11 00:00:00+01:00")])
exp = Series(
    [
        Timestamp("2012-11-11 00:00:00+01:00"),
        Timestamp("2012-11-11 00:00:00+01:00"),
    ]
)
tm.assert_series_equal(ser.fillna(method="bfill"), exp)
