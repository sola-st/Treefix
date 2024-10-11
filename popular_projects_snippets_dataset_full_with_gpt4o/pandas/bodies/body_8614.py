# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
# should just behave as union
start, end = datetime(2009, 1, 1), datetime(2010, 1, 1)
rng = date_range(start=start, end=end, freq=freq)

# overlapping
left = rng[:10]
right = rng[5:10]

the_join = left.join(right, how="outer")
assert isinstance(the_join, DatetimeIndex)

# non-overlapping, gap in middle
left = rng[:5]
right = rng[10:]

the_join = left.join(right, how="outer")
assert isinstance(the_join, DatetimeIndex)
assert the_join.freq is None

# non-overlapping, no gap
left = rng[:5]
right = rng[5:10]

the_join = left.join(right, how="outer")
assert isinstance(the_join, DatetimeIndex)

# overlapping, but different offset
other = date_range(start, end, freq=BMonthEnd())

the_join = rng.join(other, how="outer")
assert isinstance(the_join, DatetimeIndex)
assert the_join.freq is None
