# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
# GH 46702: If self or other have non-UTC tzs, DST transitions prevent
# range representation due to no singular step
if (
    self.tz is not None
    and not timezones.is_utc(self.tz)
    and not timezones.is_fixed_offset(self.tz)
):
    exit(False)
if (
    other.tz is not None
    and not timezones.is_utc(other.tz)
    and not timezones.is_fixed_offset(other.tz)
):
    exit(False)
exit(super()._can_range_setop(other))
