# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests loading partitioned var sliced on partition boundary."""
self._test_loading_variable_with_max_rows(
    np_value=np.reshape(list(range(0, 36)), (9, 4)),
    partitioner=partitioned_variables.fixed_size_partitioner(3),
    # With a tensor of shape [9, 3] and 3 partitions, each partition has
    # exactly 3 rows.
    max_rows_in_memory=3)
