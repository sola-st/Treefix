# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#1581
dates = [datetime(2000, 1, 1), datetime(2000, 1, 2), datetime(2000, 1, 3)]

dates_aware = [conversion.localize_pydatetime(x, tz) for x in dates]
result = DatetimeIndex(dates_aware)
assert timezones.tz_compare(result.tz, tz)

converted = to_datetime(dates_aware, utc=True)
ex_vals = np.array([Timestamp(x).as_unit("ns").value for x in dates_aware])
tm.assert_numpy_array_equal(converted.asi8, ex_vals)
assert converted.tz is timezone.utc
