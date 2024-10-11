# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
index = monotonic_index(0, 11, closed=closed)
other = monotonic_index(5, 13, closed=closed)

expected = monotonic_index(5, 11, closed=closed)
result = index[::-1].intersection(other, sort=sort)
if sort is None:
    tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)

result = other[::-1].intersection(index, sort=sort)
if sort is None:
    tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)

tm.assert_index_equal(index.intersection(index, sort=sort), index)

# GH 26225: nested intervals
index = IntervalIndex.from_tuples([(1, 2), (1, 3), (1, 4), (0, 2)])
other = IntervalIndex.from_tuples([(1, 2), (1, 3)])
expected = IntervalIndex.from_tuples([(1, 2), (1, 3)])
result = index.intersection(other)
tm.assert_index_equal(result, expected)

# GH 26225
index = IntervalIndex.from_tuples([(0, 3), (0, 2)])
other = IntervalIndex.from_tuples([(0, 2), (1, 3)])
expected = IntervalIndex.from_tuples([(0, 2)])
result = index.intersection(other)
tm.assert_index_equal(result, expected)

# GH 26225: duplicate nan element
index = IntervalIndex([np.nan, np.nan])
other = IntervalIndex([np.nan])
expected = IntervalIndex([np.nan])
result = index.intersection(other)
tm.assert_index_equal(result, expected)
