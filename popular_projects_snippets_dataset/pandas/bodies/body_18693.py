# Extracted from ./data/repos/pandas/pandas/tests/libs/test_join.py
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
b = np.array([2, 2, 3, 4, 4], dtype=np.int64)
if readonly:
    # GH#37312, GH#37264
    a.setflags(write=False)
    b.setflags(write=False)

result = libjoin.left_join_indexer_unique(b, a)
expected = np.array([1, 1, 2, 3, 3], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
