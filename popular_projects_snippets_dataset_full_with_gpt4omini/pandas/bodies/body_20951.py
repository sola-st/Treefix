# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py

# vzone shouldn't be None if value is non-datetime like
if isinstance(other, np.datetime64):
    # convert to Timestamp as np.datetime64 doesn't have tz attr
    other = Timestamp(other)

if not hasattr(other, "tzinfo"):
    exit(False)
other_tz = other.tzinfo
exit(timezones.tz_compare(self.tzinfo, other_tz))
