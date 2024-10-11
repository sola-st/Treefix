# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng = date_range("1/1/2000", periods=50, freq=Minute())
rng1 = rng[10:]
rng2 = rng[:25]
the_union = rng1.union(rng2, sort=sort)
if sort is None:
    tm.assert_index_equal(the_union, rng)
else:
    expected = DatetimeIndex(list(rng[10:]) + list(rng[:10]))
    tm.assert_index_equal(the_union, expected)

rng1 = rng[10:]
rng2 = rng[15:35]
the_union = rng1.union(rng2, sort=sort)
expected = rng[10:]
tm.assert_index_equal(the_union, expected)
