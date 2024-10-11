# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mat = _as_array(mgr)
taken = mgr.take(indexer, axis)
tm.assert_numpy_array_equal(
    np.take(mat, indexer, axis), _as_array(taken), check_dtype=False
)
tm.assert_index_equal(mgr.axes[axis].take(indexer), taken.axes[axis])
