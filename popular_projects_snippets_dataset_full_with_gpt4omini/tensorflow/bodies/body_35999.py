# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[4, 0])
self.assertEqual(4, partition_info.single_offset([1, 3]))

# Tests when the variable isn't partitioned at all.
partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[0, 0])
self.assertEqual(0, partition_info.single_offset([9, 3]))
