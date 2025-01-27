# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#17943, GH#17690, GH#5168
stamps = [
    Timestamp(year=2017, month=10, day=22, tz="UTC"),
    Timestamp(year=2017, month=10, day=22, tzinfo=pytz.utc),
    Timestamp(year=2017, month=10, day=22, tz=pytz.utc),
    Timestamp(datetime(2017, 10, 22), tzinfo=pytz.utc),
    Timestamp(datetime(2017, 10, 22), tz="UTC"),
    Timestamp(datetime(2017, 10, 22), tz=pytz.utc),
]
assert all(ts == stamps[0] for ts in stamps)
