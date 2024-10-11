# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
parsed, reso = super()._parse_with_reso(label)

parsed = Timestamp(parsed)

if self.tz is not None and parsed.tzinfo is None:
    # we special-case timezone-naive strings and timezone-aware
    #  DatetimeIndex
    # https://github.com/pandas-dev/pandas/pull/36148#issuecomment-687883081
    parsed = parsed.tz_localize(self.tz)

exit((parsed, reso))
