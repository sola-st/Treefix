# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# Localizing to time zone should:
#  1) check for DST ambiguities
#  2) convert to UTC

rng = date_range("3/10/2012", "3/11/2012", freq="30T")

converted = rng.tz_localize(tz)
expected_naive = rng + pd.offsets.Hour(5)
tm.assert_numpy_array_equal(converted.asi8, expected_naive.asi8)

# DST ambiguity, this should fail
rng = date_range("3/11/2012", "3/12/2012", freq="30T")
# Is this really how it should fail??
with pytest.raises(pytz.NonExistentTimeError, match="2012-03-11 02:00:00"):
    rng.tz_localize(tz)
