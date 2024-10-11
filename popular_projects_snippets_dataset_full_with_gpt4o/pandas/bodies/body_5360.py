# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# validate that pytz and dateutil are compat for dst
# when the transition happens
naive = Timestamp("2013-10-27 01:00:00")

pytz_zone = "Europe/London"
dateutil_zone = "dateutil/Europe/London"
result_pytz = naive.tz_localize(pytz_zone, ambiguous=False)
result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=False)
assert result_pytz.value == result_dateutil.value
assert result_pytz.value == 1382835600

# fixed ambiguous behavior
# see gh-14621, GH#45087
assert result_pytz.to_pydatetime().tzname() == "GMT"
assert result_dateutil.to_pydatetime().tzname() == "GMT"
assert str(result_pytz) == str(result_dateutil)

# 1 hour difference
result_pytz = naive.tz_localize(pytz_zone, ambiguous=True)
result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=True)
assert result_pytz.value == result_dateutil.value
assert result_pytz.value == 1382832000

# see gh-14621
assert str(result_pytz) == str(result_dateutil)
assert (
    result_pytz.to_pydatetime().tzname()
    == result_dateutil.to_pydatetime().tzname()
)
