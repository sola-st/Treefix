# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
tm.assert_numpy_array_equal(left.values, right.values)
assert left.dtype == right.dtype
assert isinstance(left.mgr_locs, BlockPlacement)
assert isinstance(right.mgr_locs, BlockPlacement)
tm.assert_numpy_array_equal(left.mgr_locs.as_array, right.mgr_locs.as_array)
