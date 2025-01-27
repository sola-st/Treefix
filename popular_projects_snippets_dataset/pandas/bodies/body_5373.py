# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH#1389

# 4 hours before DST transition
stamp = Timestamp("3/10/2012 22:00", tz=tz)

result = stamp + timedelta(hours=6)

# spring forward, + "7" hours
expected = Timestamp("3/11/2012 05:00", tz=tz)

assert result == expected
