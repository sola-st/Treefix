# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests loading normal var as a single slice with no valid max_rows."""
self._test_loading_variable_with_max_rows(
    np_value=np.reshape(list(range(0, 18)), (6, 3)),
    partitioner=None,
    max_rows_in_memory=-1)
