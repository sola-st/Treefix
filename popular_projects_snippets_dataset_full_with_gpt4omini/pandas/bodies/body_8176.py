# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# November 6, 2011, fall back, repeat 2 AM hour
# With no repeated hours, we cannot infer the transition
dr = date_range(datetime(2011, 11, 6, 0), periods=5, freq=pd.offsets.Hour())
with pytest.raises(pytz.AmbiguousTimeError, match="Cannot infer dst time"):
    dr.tz_localize(tz)

# With repeated hours, we can infer the transition
dr = date_range(
    datetime(2011, 11, 6, 0), periods=5, freq=pd.offsets.Hour(), tz=tz
)
times = [
    "11/06/2011 00:00",
    "11/06/2011 01:00",
    "11/06/2011 01:00",
    "11/06/2011 02:00",
    "11/06/2011 03:00",
]
di = DatetimeIndex(times)
localized = di.tz_localize(tz, ambiguous="infer")
expected = dr._with_freq(None)
tm.assert_index_equal(expected, localized)
tm.assert_index_equal(expected, DatetimeIndex(times, tz=tz, ambiguous="infer"))

# When there is no dst transition, nothing special happens
dr = date_range(datetime(2011, 6, 1, 0), periods=10, freq=pd.offsets.Hour())
localized = dr.tz_localize(tz)
localized_infer = dr.tz_localize(tz, ambiguous="infer")
tm.assert_index_equal(localized, localized_infer)
