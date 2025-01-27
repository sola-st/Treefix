# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
def assert_reindex_axis_is_ok(mgr, axis, new_labels, fill_value):
    mat = _as_array(mgr)
    indexer = mgr.axes[axis].get_indexer_for(new_labels)

    reindexed = mgr.reindex_axis(new_labels, axis, fill_value=fill_value)
    tm.assert_numpy_array_equal(
        algos.take_nd(mat, indexer, axis, fill_value=fill_value),
        _as_array(reindexed),
        check_dtype=False,
    )
    tm.assert_index_equal(reindexed.axes[axis], new_labels)

for ax in range(mgr.ndim):
    assert_reindex_axis_is_ok(mgr, ax, Index([]), fill_value)
    assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax], fill_value)
    assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][[0, 0, 0]], fill_value)
    assert_reindex_axis_is_ok(mgr, ax, Index(["foo", "bar", "baz"]), fill_value)
    assert_reindex_axis_is_ok(
        mgr, ax, Index(["foo", mgr.axes[ax][0], "baz"]), fill_value
    )

    if mgr.shape[ax] >= 3:
        assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][:-3], fill_value)
        assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][-3::-1], fill_value)
        assert_reindex_axis_is_ok(
            mgr, ax, mgr.axes[ax][[0, 1, 2, 0, 1, 2]], fill_value
        )
