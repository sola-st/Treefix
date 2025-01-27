# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 8689
ser = Series(date_range("20130101", periods=5, freq="D"))
ser.iloc[2] = pd.NaT

for attr in ["microsecond", "nanosecond", "second", "minute", "hour", "day"]:
    expected = getattr(ser.dt, attr).copy()
    expected.iloc[2] = np.nan
    result = getattr(ser.dt, attr)
    tm.assert_series_equal(result, expected)

result = ser.dt.date
expected = Series(
    [
        date(2013, 1, 1),
        date(2013, 1, 2),
        np.nan,
        date(2013, 1, 4),
        date(2013, 1, 5),
    ],
    dtype="object",
)
tm.assert_series_equal(result, expected)

result = ser.dt.time
expected = Series([time(0), time(0), np.nan, time(0), time(0)], dtype="object")
tm.assert_series_equal(result, expected)
