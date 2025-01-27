# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# intersection of non-overlapping values based on start value and gcd
index = RangeIndex(1, 10, 2, name=names[0])
other = RangeIndex(0, 10, 4, name=names[1])
result = index.intersection(other, sort=sort)
expected = RangeIndex(0, 0, 1, name=names[2])
tm.assert_index_equal(result, expected)
