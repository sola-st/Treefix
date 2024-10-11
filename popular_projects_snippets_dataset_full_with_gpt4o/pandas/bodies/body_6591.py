# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# GH#44019
left = RangeIndex(range(0, 20, 4))
right = RangeIndex(range(1, 21, 4))

result = left.union(right)
expected = Index([0, 1, 4, 5, 8, 9, 12, 13, 16, 17])
tm.assert_index_equal(result, expected, exact=True)
