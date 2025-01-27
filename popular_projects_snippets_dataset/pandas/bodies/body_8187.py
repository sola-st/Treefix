# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# construction with an nonexistent end-point

with pytest.raises(pytz.NonExistentTimeError, match="2019-03-10 02:00:00"):
    date_range(
        "2019-03-10 00:00", "2019-03-10 02:00", tz="US/Pacific", freq="H"
    )

times = date_range(
    "2019-03-10 00:00", "2019-03-10 02:00", freq="H", tz=tz, nonexistent=option
)
assert times[-1] == Timestamp(expected, tz=tz)
