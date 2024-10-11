# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#43212 `value` is also a MultiIndex

left = MultiIndex.from_tuples([(np.nan, 6), (np.nan, 6), ("a", 4)])
right = MultiIndex.from_tuples([("a", 1), ("a", 1), ("d", 1)])
mask = np.array([True, True, False])

result = left.putmask(mask, right)

expected = MultiIndex.from_tuples([right[0], right[1], left[2]])
tm.assert_index_equal(result, expected)
