# Extracted from ./data/repos/pandas/pandas/tests/libs/test_join.py
indexer = libjoin.outer_join_indexer

left = np.arange(3, dtype=dtype)
right = np.arange(2, 5, dtype=dtype)
empty = np.array([], dtype=dtype)

result, lindexer, rindexer = indexer(left, right)
assert isinstance(result, np.ndarray)
assert isinstance(lindexer, np.ndarray)
assert isinstance(rindexer, np.ndarray)
tm.assert_numpy_array_equal(result, np.arange(5, dtype=dtype))
exp = np.array([0, 1, 2, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(lindexer, exp)
exp = np.array([-1, -1, 0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(rindexer, exp)

result, lindexer, rindexer = indexer(empty, right)
tm.assert_numpy_array_equal(result, right)
exp = np.array([-1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(lindexer, exp)
exp = np.array([0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(rindexer, exp)

result, lindexer, rindexer = indexer(left, empty)
tm.assert_numpy_array_equal(result, left)
exp = np.array([0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(lindexer, exp)
exp = np.array([-1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(rindexer, exp)
