# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
off = FixedOffset(420, "+07:00")
start = datetime(2012, 3, 11, 5, 0, 0, tzinfo=off)
end = datetime(2012, 6, 11, 5, 0, 0, tzinfo=off)
rng = date_range(start=start, end=end)
assert off == rng.tz

rng2 = date_range(start, periods=len(rng), tz=off)
tm.assert_index_equal(rng, rng2)

rng3 = date_range("3/11/2012 05:00:00+07:00", "6/11/2012 05:00:00+07:00")
assert (rng.values == rng3.values).all()
