# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests loading partitioned var as a single slice.

    (When the specified max_rows_in_memory is larger than the number of rows)
    """
self._test_loading_variable_with_max_rows(
    np_value=np.reshape(list(range(0, 36)), (9, 4)),
    partitioner=partitioned_variables.fixed_size_partitioner(3),
    max_rows_in_memory=10)
