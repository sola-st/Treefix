# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_indexing.py
# GH#43240
idx = RangeIndex(0, 5, name="test")

mask = np.array([True, True, False, False, False])
result = idx.putmask(mask, 10)
expected = Index([10, 10, 2, 3, 4], dtype=np.int64, name="test")
tm.assert_index_equal(result, expected)

result = idx.where(~mask, 10)
tm.assert_index_equal(result, expected)
