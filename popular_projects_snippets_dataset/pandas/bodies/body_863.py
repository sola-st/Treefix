# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
def assert_slice_ok(mgr, axis, slobj):
    mat = _as_array(mgr)

    # we maybe using an ndarray to test slicing and
    # might not be the full length of the axis
    if isinstance(slobj, np.ndarray):
        ax = mgr.axes[axis]
        if len(ax) and len(slobj) and len(slobj) != len(ax):
            slobj = np.concatenate(
                [slobj, np.zeros(len(ax) - len(slobj), dtype=bool)]
            )

    if isinstance(slobj, slice):
        sliced = mgr.get_slice(slobj, axis=axis)
    elif mgr.ndim == 1 and axis == 0:
        sliced = mgr.getitem_mgr(slobj)
    else:
        # BlockManager doesn't support non-slice, SingleBlockManager
        #  doesn't support axis > 0
        exit()

    mat_slobj = (slice(None),) * axis + (slobj,)
    tm.assert_numpy_array_equal(
        mat[mat_slobj], _as_array(sliced), check_dtype=False
    )
    tm.assert_index_equal(mgr.axes[axis][slobj], sliced.axes[axis])

assert mgr.ndim <= 2, mgr.ndim
for ax in range(mgr.ndim):
    # slice
    assert_slice_ok(mgr, ax, slice(None))
    assert_slice_ok(mgr, ax, slice(3))
    assert_slice_ok(mgr, ax, slice(100))
    assert_slice_ok(mgr, ax, slice(1, 4))
    assert_slice_ok(mgr, ax, slice(3, 0, -2))

    if mgr.ndim < 2:
        # 2D only support slice objects

        # boolean mask
        assert_slice_ok(mgr, ax, np.array([], dtype=np.bool_))
        assert_slice_ok(mgr, ax, np.ones(mgr.shape[ax], dtype=np.bool_))
        assert_slice_ok(mgr, ax, np.zeros(mgr.shape[ax], dtype=np.bool_))

        if mgr.shape[ax] >= 3:
            assert_slice_ok(mgr, ax, np.arange(mgr.shape[ax]) % 3 == 0)
            assert_slice_ok(
                mgr, ax, np.array([True, True, False], dtype=np.bool_)
            )

        # fancy indexer
        assert_slice_ok(mgr, ax, [])
        assert_slice_ok(mgr, ax, list(range(mgr.shape[ax])))

        if mgr.shape[ax] >= 3:
            assert_slice_ok(mgr, ax, [0, 1, 2])
            assert_slice_ok(mgr, ax, [-1, -2, -3])
