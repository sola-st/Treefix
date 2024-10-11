# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = RangeIndex(0, 6, 1)

loc = [0, 1, 2, 3, 4, 5]
result = idx.delete(loc)
expected = idx[:0]
tm.assert_index_equal(result, expected, exact=True)

result = idx.delete(loc[::-1])
tm.assert_index_equal(result, expected, exact=True)
