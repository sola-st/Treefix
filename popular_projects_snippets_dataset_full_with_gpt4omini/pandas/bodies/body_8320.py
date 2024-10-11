# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng = bdate_range(START, END)
# overlapping
left = rng[:10]
right = rng[5:10]

the_union = left.union(right, sort=sort)
assert isinstance(the_union, DatetimeIndex)

# non-overlapping, gap in middle
left = rng[:5]
right = rng[10:]

the_union = left.union(right, sort=sort)
assert isinstance(the_union, Index)

# non-overlapping, no gap
left = rng[:5]
right = rng[5:10]

the_union = left.union(right, sort=sort)
assert isinstance(the_union, DatetimeIndex)

# order does not matter
if sort is None:
    tm.assert_index_equal(right.union(left, sort=sort), the_union)
else:
    expected = DatetimeIndex(list(right) + list(left))
    tm.assert_index_equal(right.union(left, sort=sort), expected)

# overlapping, but different offset
rng = date_range(START, END, freq=BMonthEnd())

the_union = rng.union(rng, sort=sort)
assert isinstance(the_union, DatetimeIndex)
