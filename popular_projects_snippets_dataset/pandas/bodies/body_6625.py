# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
idx = RangeIndex(0, 6, 1)

loc = [2, 3, 4, 5]
result = idx.delete(loc)
expected = idx[:2]
tm.assert_index_equal(result, expected, exact=True)

result = idx.delete(loc[::-1])
tm.assert_index_equal(result, expected, exact=True)
