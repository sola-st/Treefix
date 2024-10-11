# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
times = [
    "11/06/2011 00:00",
    "11/06/2011 01:00",
    "11/06/2011 01:00",
    "11/06/2011 02:00",
    "11/06/2011 03:00",
]
di = DatetimeIndex(times)
localized = di.tz_localize(tz, ambiguous="NaT")

times = [
    "11/06/2011 00:00",
    np.NaN,
    np.NaN,
    "11/06/2011 02:00",
    "11/06/2011 03:00",
]
di_test = DatetimeIndex(times, tz="US/Eastern")

# left dtype is datetime64[ns, US/Eastern]
# right is datetime64[ns, tzfile('/usr/share/zoneinfo/US/Eastern')]
tm.assert_numpy_array_equal(di_test.values, localized.values)
