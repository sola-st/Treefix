# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# https://github.com/pandas-dev/pandas/issues/38851
# different tzinfos representing UTC treated as equal
ser = Series(date_range("2020", periods=3, tz="UTC"))
expected = ser.copy()
ser[1] = NaT
result = ser.fillna(datetime(2020, 1, 2, tzinfo=timezone.utc))
tm.assert_series_equal(result, expected)

# pre-2.0 we cast to object with mixed tzs, in 2.0 we retain dtype
ts = Timestamp("2000-01-01", tz="US/Pacific")
ser2 = Series(ser._values.tz_convert("dateutil/US/Pacific"))
assert ser2.dtype.kind == "M"
result = ser2.fillna(ts)
expected = Series(
    [ser2[0], ts.tz_convert(ser2.dtype.tz), ser2[2]],
    dtype=ser2.dtype,
)
tm.assert_series_equal(result, expected)
