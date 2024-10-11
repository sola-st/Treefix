# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# make sure that we are not re-localizing upon construction
# GH 14928
ser = Series(date_range("20130101", periods=3, tz="US/Eastern"))

result = Series(ser, dtype=ser.dtype)
tm.assert_series_equal(result, ser)

result = Series(ser.dt.tz_convert("UTC"), dtype=ser.dtype)
tm.assert_series_equal(result, ser)

# Pre-2.0 dt64 values were treated as utc, which was inconsistent
#  with DatetimeIndex, which treats them as wall times, see GH#33401
result = Series(ser.values, dtype=ser.dtype)
expected = Series(ser.values).dt.tz_localize(ser.dtype.tz)
tm.assert_series_equal(result, expected)

with tm.assert_produces_warning(None):
    # one suggested alternative to the deprecated (changed in 2.0) usage
    middle = Series(ser.values).dt.tz_localize("UTC")
    result = middle.dt.tz_convert(ser.dtype.tz)
tm.assert_series_equal(result, ser)

with tm.assert_produces_warning(None):
    # the other suggested alternative to the deprecated usage
    result = Series(ser.values.view("int64"), dtype=ser.dtype)
tm.assert_series_equal(result, ser)
