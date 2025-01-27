# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests loading partitioned var with more slices than partitions."""
self._test_loading_variable_with_max_rows(
    np_value=np.reshape(list(range(0, 36)), (9, 4)),
    partitioner=partitioned_variables.fixed_size_partitioner(3),
    # Even though each partition has 3 rows, we'll only load the tensor one
    # row at a time.
    max_rows_in_memory=1)
