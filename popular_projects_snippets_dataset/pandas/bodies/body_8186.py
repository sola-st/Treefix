# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# construction with an ambiguous end-point
# GH#11626

with pytest.raises(pytz.AmbiguousTimeError, match="Cannot infer dst time"):
    date_range(
        "2013-10-26 23:00", "2013-10-27 01:00", tz="Europe/London", freq="H"
    )

times = date_range(
    "2013-10-26 23:00", "2013-10-27 01:00", freq="H", tz=tz, ambiguous="infer"
)
assert times[0] == Timestamp("2013-10-26 23:00", tz=tz)
assert times[-1] == Timestamp("2013-10-27 01:00:00+0000", tz=tz)
