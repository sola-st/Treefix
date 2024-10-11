# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
index1 = MultiIndex.from_tuples(zip(["foo", "bar", "baz"], [1, 2, 3]))
index2 = MultiIndex.from_tuples([("foo", 1), ("bar", 3)])
result = index1.symmetric_difference(index2, sort=sort)
expected = MultiIndex.from_tuples([("bar", 2), ("baz", 3), ("bar", 3)])
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)
