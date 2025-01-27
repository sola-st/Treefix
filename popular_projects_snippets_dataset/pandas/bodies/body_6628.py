# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = RangeIndex(0, 6, 1)

loc = [0, 3, 5]
result = idx.delete(loc)
expected = Index([1, 2, 4])
tm.assert_index_equal(result, expected, exact=True)

result = idx.delete(loc[::-1])
tm.assert_index_equal(result, expected, exact=True)
