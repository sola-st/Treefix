# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
# overlapping
rng = bdate_range(START, END, freq="C")
left = rng[:10]
right = rng[5:10]

the_union = left.union(right, sort=sort)
assert isinstance(the_union, DatetimeIndex)

# non-overlapping, gap in middle
left = rng[:5]
right = rng[10:]

the_union = left.union(right, sort)
assert isinstance(the_union, Index)

# non-overlapping, no gap
left = rng[:5]
right = rng[5:10]

the_union = left.union(right, sort=sort)
assert isinstance(the_union, DatetimeIndex)

# order does not matter
if sort is None:
    tm.assert_index_equal(right.union(left, sort=sort), the_union)

# overlapping, but different offset
rng = date_range(START, END, freq=BMonthEnd())

the_union = rng.union(rng, sort=sort)
assert isinstance(the_union, DatetimeIndex)
