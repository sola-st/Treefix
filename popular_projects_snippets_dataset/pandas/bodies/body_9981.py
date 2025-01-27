# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
# GH 43267
indexer = FixedForwardWindowIndexer(window_size=window_size)
start, end = indexer.get_window_bounds(num_values=num_values, step=step)

tm.assert_numpy_array_equal(
    start, np.array(expected_start[::step]), check_dtype=False
)
tm.assert_numpy_array_equal(end, np.array(expected_end[::step]), check_dtype=False)
assert len(start) == len(end)
