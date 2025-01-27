# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
def assert_reindex_indexer_is_ok(mgr, axis, new_labels, indexer, fill_value):
    mat = _as_array(mgr)
    reindexed_mat = algos.take_nd(mat, indexer, axis, fill_value=fill_value)
    reindexed = mgr.reindex_indexer(
        new_labels, indexer, axis, fill_value=fill_value
    )
    tm.assert_numpy_array_equal(
        reindexed_mat, _as_array(reindexed), check_dtype=False
    )
    tm.assert_index_equal(reindexed.axes[axis], new_labels)

for ax in range(mgr.ndim):
    assert_reindex_indexer_is_ok(
        mgr, ax, Index([]), np.array([], dtype=np.intp), fill_value
    )
    assert_reindex_indexer_is_ok(
        mgr, ax, mgr.axes[ax], np.arange(mgr.shape[ax]), fill_value
    )
    assert_reindex_indexer_is_ok(
        mgr,
        ax,
        Index(["foo"] * mgr.shape[ax]),
        np.arange(mgr.shape[ax]),
        fill_value,
    )
    assert_reindex_indexer_is_ok(
        mgr, ax, mgr.axes[ax][::-1], np.arange(mgr.shape[ax]), fill_value
    )
    assert_reindex_indexer_is_ok(
        mgr, ax, mgr.axes[ax], np.arange(mgr.shape[ax])[::-1], fill_value
    )
    assert_reindex_indexer_is_ok(
        mgr, ax, Index(["foo", "bar", "baz"]), np.array([0, 0, 0]), fill_value
    )
    assert_reindex_indexer_is_ok(
        mgr, ax, Index(["foo", "bar", "baz"]), np.array([-1, 0, -1]), fill_value
    )
    assert_reindex_indexer_is_ok(
        mgr,
        ax,
        Index(["foo", mgr.axes[ax][0], "baz"]),
        np.array([-1, -1, -1]),
        fill_value,
    )

    if mgr.shape[ax] >= 3:
        assert_reindex_indexer_is_ok(
            mgr,
            ax,
            Index(["foo", "bar", "baz"]),
            np.array([0, 1, 2]),
            fill_value,
        )
