# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#13057
times = ["2015-03-08 01:00", "2015-03-08 02:00", "2015-03-08 03:00"]
index = DatetimeIndex(times)
tz = "US/Eastern"
with pytest.raises(pytz.NonExistentTimeError, match="|".join(times)):
    index.tz_localize(tz=tz)

with pytest.raises(pytz.NonExistentTimeError, match="|".join(times)):
    index.tz_localize(tz=tz, nonexistent="raise")

result = index.tz_localize(tz=tz, nonexistent="NaT")
test_times = ["2015-03-08 01:00-05:00", "NaT", "2015-03-08 03:00-04:00"]
dti = to_datetime(test_times, utc=True)
expected = dti.tz_convert("US/Eastern")
tm.assert_index_equal(result, expected)
