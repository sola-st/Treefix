# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng = date_range("1/1/2000", periods=50, freq=Minute())
rng1 = rng[10:]
rng2 = rng[:25]
the_int = rng1.intersection(rng2)
expected = rng[10:25]
tm.assert_index_equal(the_int, expected)
assert isinstance(the_int, DatetimeIndex)
assert the_int.freq == rng.freq

the_int = rng1.intersection(rng2.view(DatetimeIndex))
tm.assert_index_equal(the_int, expected)

# non-overlapping
the_int = rng[:10].intersection(rng[10:])
expected = DatetimeIndex([])
tm.assert_index_equal(the_int, expected)
