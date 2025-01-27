# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mat = _as_array(mgr)
reindexed_mat = algos.take_nd(mat, indexer, axis, fill_value=fill_value)
reindexed = mgr.reindex_indexer(
    new_labels, indexer, axis, fill_value=fill_value
)
tm.assert_numpy_array_equal(
    reindexed_mat, _as_array(reindexed), check_dtype=False
)
tm.assert_index_equal(reindexed.axes[axis], new_labels)
