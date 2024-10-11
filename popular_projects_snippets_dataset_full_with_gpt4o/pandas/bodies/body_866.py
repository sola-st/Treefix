# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mat = _as_array(mgr)
indexer = mgr.axes[axis].get_indexer_for(new_labels)

reindexed = mgr.reindex_axis(new_labels, axis, fill_value=fill_value)
tm.assert_numpy_array_equal(
    algos.take_nd(mat, indexer, axis, fill_value=fill_value),
    _as_array(reindexed),
    check_dtype=False,
)
tm.assert_index_equal(reindexed.axes[axis], new_labels)
