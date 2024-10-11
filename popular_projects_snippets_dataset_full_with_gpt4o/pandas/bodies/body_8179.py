# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
tzstr = prefix + "US/Eastern"
dti = date_range(start="1/1/2005", end="1/1/2005 0:00:30.256", freq="L")
dti2 = dti.tz_localize(tzstr)

dti_utc = date_range(
    start="1/1/2005 05:00", end="1/1/2005 5:00:30.256", freq="L", tz="utc"
)

tm.assert_numpy_array_equal(dti2.values, dti_utc.values)

dti3 = dti2.tz_convert(prefix + "US/Pacific")
tm.assert_numpy_array_equal(dti3.values, dti_utc.values)

dti = date_range(start="11/6/2011 1:59", end="11/6/2011 2:00", freq="L")
with pytest.raises(pytz.AmbiguousTimeError, match="Cannot infer dst time"):
    dti.tz_localize(tzstr)

dti = date_range(start="3/13/2011 1:59", end="3/13/2011 2:00", freq="L")
with pytest.raises(pytz.NonExistentTimeError, match="2011-03-13 02:00:00"):
    dti.tz_localize(tzstr)
