# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# see GH#6572: ISO 8601 format results in stdlib timezone object
idx = date_range(
    "2013-01-01T00:00:00-05:00", "2016-01-01T23:59:59-05:00", freq=freq
)
expected = date_range(
    "2013-01-01T00:00:00",
    "2016-01-01T23:59:59",
    freq=freq,
    tz=timezone(timedelta(minutes=-300)),
)
tm.assert_index_equal(idx, expected)
# Unable to use `US/Eastern` because of DST
expected_i8 = date_range(
    "2013-01-01T00:00:00", "2016-01-01T23:59:59", freq=freq, tz="America/Lima"
)
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)

idx = date_range(
    "2013-01-01T00:00:00+09:00", "2016-01-01T23:59:59+09:00", freq=freq
)
expected = date_range(
    "2013-01-01T00:00:00",
    "2016-01-01T23:59:59",
    freq=freq,
    tz=timezone(timedelta(minutes=540)),
)
tm.assert_index_equal(idx, expected)
expected_i8 = date_range(
    "2013-01-01T00:00:00", "2016-01-01T23:59:59", freq=freq, tz="Asia/Tokyo"
)
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)

# Non ISO 8601 format results in dateutil.tz.tzoffset
idx = date_range("2013/1/1 0:00:00-5:00", "2016/1/1 23:59:59-5:00", freq=freq)
expected = date_range(
    "2013-01-01T00:00:00",
    "2016-01-01T23:59:59",
    freq=freq,
    tz=timezone(timedelta(minutes=-300)),
)
tm.assert_index_equal(idx, expected)
# Unable to use `US/Eastern` because of DST
expected_i8 = date_range(
    "2013-01-01T00:00:00", "2016-01-01T23:59:59", freq=freq, tz="America/Lima"
)
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)

idx = date_range("2013/1/1 0:00:00+9:00", "2016/1/1 23:59:59+09:00", freq=freq)
expected = date_range(
    "2013-01-01T00:00:00",
    "2016-01-01T23:59:59",
    freq=freq,
    tz=timezone(timedelta(minutes=540)),
)
tm.assert_index_equal(idx, expected)
expected_i8 = date_range(
    "2013-01-01T00:00:00", "2016-01-01T23:59:59", freq=freq, tz="Asia/Tokyo"
)
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
