# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests loading normal var when rows are evenly divisible by max_rows."""
self._test_loading_variable_with_max_rows(
    np_value=np.reshape(list(range(0, 36)), (9, 4)),
    partitioner=None,
    # 9 is evenly divisible by 3.
    max_rows_in_memory=3)
