# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
left = RangeIndex(range(4))
right = RangeIndex(range(1, 3))

result = left.difference(right)
expected = RangeIndex(0, 4, 3)
assert expected.tolist() == [0, 3]
tm.assert_index_equal(result, expected, exact=True)
