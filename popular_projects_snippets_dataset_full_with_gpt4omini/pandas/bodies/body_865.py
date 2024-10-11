# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
def assert_take_ok(mgr, axis, indexer):
    mat = _as_array(mgr)
    taken = mgr.take(indexer, axis)
    tm.assert_numpy_array_equal(
        np.take(mat, indexer, axis), _as_array(taken), check_dtype=False
    )
    tm.assert_index_equal(mgr.axes[axis].take(indexer), taken.axes[axis])

for ax in range(mgr.ndim):
    # take/fancy indexer
    assert_take_ok(mgr, ax, indexer=[])
    assert_take_ok(mgr, ax, indexer=[0, 0, 0])
    assert_take_ok(mgr, ax, indexer=list(range(mgr.shape[ax])))

    if mgr.shape[ax] >= 3:
        assert_take_ok(mgr, ax, indexer=[0, 1, 2])
        assert_take_ok(mgr, ax, indexer=[-1, -2, -3])
