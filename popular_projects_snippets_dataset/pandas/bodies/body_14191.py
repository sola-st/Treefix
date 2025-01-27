# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Formatting periods created from a datetime with timezone.

# This timestamp is in 2013 in Europe/Paris but is 2012 in UTC
dt = pd.to_datetime(["2013-01-01 00:00:00+01:00"], utc=True)

# Converting to a period looses the timezone information
# Since tz is currently set as utc, we'll see 2012
with tm.assert_produces_warning(UserWarning, match="will drop timezone"):
    per = dt.to_period(freq="H")
assert per.format()[0] == "2012-12-31 23:00"

# If tz is currently set as paris before conversion, we'll see 2013
dt = dt.tz_convert("Europe/Paris")
with tm.assert_produces_warning(UserWarning, match="will drop timezone"):
    per = dt.to_period(freq="H")
assert per.format()[0] == "2013-01-01 00:00"
