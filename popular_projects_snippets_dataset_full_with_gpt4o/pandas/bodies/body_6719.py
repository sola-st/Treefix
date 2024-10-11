# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
index = monotonic_index(0, 11, closed=closed)
other = monotonic_index(5, 13, closed=closed)

expected = monotonic_index(0, 13, closed=closed)
result = index[::-1].union(other, sort=sort)
if sort is None:
    tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)

result = other[::-1].union(index, sort=sort)
if sort is None:
    tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)

tm.assert_index_equal(index.union(index, sort=sort), index)
tm.assert_index_equal(index.union(index[:1], sort=sort), index)
