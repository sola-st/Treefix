# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng1 = date_range("1/1/2000", freq="D", periods=5, tz=tz)
other1 = date_range("1/6/2000", freq="D", periods=5, tz=tz)
expected1 = date_range("1/1/2000", freq="D", periods=10, tz=tz)
expected1_notsorted = DatetimeIndex(list(other1) + list(rng1))

rng2 = date_range("1/1/2000", freq="D", periods=5, tz=tz)
other2 = date_range("1/4/2000", freq="D", periods=5, tz=tz)
expected2 = date_range("1/1/2000", freq="D", periods=8, tz=tz)
expected2_notsorted = DatetimeIndex(list(other2) + list(rng2[:3]))

rng3 = date_range("1/1/2000", freq="D", periods=5, tz=tz)
other3 = DatetimeIndex([], tz=tz)
expected3 = date_range("1/1/2000", freq="D", periods=5, tz=tz)
expected3_notsorted = rng3

for rng, other, exp, exp_notsorted in [
    (rng1, other1, expected1, expected1_notsorted),
    (rng2, other2, expected2, expected2_notsorted),
    (rng3, other3, expected3, expected3_notsorted),
]:

    result_union = rng.union(other, sort=sort)
    tm.assert_index_equal(result_union, exp)

    result_union = other.union(rng, sort=sort)
    if sort is None:
        tm.assert_index_equal(result_union, exp)
    else:
        tm.assert_index_equal(result_union, exp_notsorted)
