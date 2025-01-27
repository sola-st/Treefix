# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
assert isinstance(fblock.mgr_locs, BlockPlacement)
tm.assert_numpy_array_equal(
    fblock.mgr_locs.as_array, np.array([0, 2, 4], dtype=np.intp)
)
