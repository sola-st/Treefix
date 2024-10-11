# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
tm.assert_numpy_array_equal(
    BlockPlacement(slc).as_array, np.asarray(arr, dtype=np.intp)
)
