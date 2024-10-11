# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng_a = date_range("1/1/2012", periods=4, freq="3H")
rng_b = date_range("1/1/2012", periods=4, freq="4H")

result = rng_a.union(rng_b, sort=sort)
exp = list(rng_a) + list(rng_b[1:])
if sort is None:
    exp = DatetimeIndex(sorted(exp))
else:
    exp = DatetimeIndex(exp)
tm.assert_index_equal(result, exp)
