# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
offset = DateOffset(**{offset_name: offset_n})

t = tstart + offset
if expected_utc_offset is not None:
    assert get_utc_offset_hours(t) == expected_utc_offset

if offset_name == "weeks":
    # dates should match
    assert t.date() == timedelta(days=7 * offset.kwds["weeks"]) + tstart.date()
    # expect the same day of week, hour of day, minute, second, ...
    assert (
        t.dayofweek == tstart.dayofweek
        and t.hour == tstart.hour
        and t.minute == tstart.minute
        and t.second == tstart.second
    )
elif offset_name == "days":
    # dates should match
    assert timedelta(offset.kwds["days"]) + tstart.date() == t.date()
    # expect the same hour of day, minute, second, ...
    assert (
        t.hour == tstart.hour
        and t.minute == tstart.minute
        and t.second == tstart.second
    )
elif offset_name in self.valid_date_offsets_singular:
    # expect the singular offset value to match between tstart and t
    datepart_offset = getattr(
        t, offset_name if offset_name != "weekday" else "dayofweek"
    )
    assert datepart_offset == offset.kwds[offset_name]
else:
    # the offset should be the same as if it was done in UTC
    assert t == (tstart.tz_convert("UTC") + offset).tz_convert("US/Pacific")
