# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
left = RangeIndex(-8, 20, 7)
right = RangeIndex(13, -9, -3)

result = left.difference(right)
expected = RangeIndex(-1, 13, 7)
assert expected.tolist() == [-1, 6]
tm.assert_index_equal(result, expected, exact=True)
