# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[4, 0])
# Invalid shape.
with self.assertRaises(TypeError):
    partition_info.single_slice_dim(None)

# Rank of shape differs from full_shape.
with self.assertRaises(ValueError):
    partition_info.single_slice_dim([1, 2, 3])

# Shape is too large given var_offset (4+6 > 9).
with self.assertRaises(ValueError):
    partition_info.single_slice_dim([6, 3])

# Multiple possible slice dim from shape.
with self.assertRaises(ValueError):
    partition_info.single_slice_dim([1, 1])

partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[0, 0])
self.assertEqual(1, partition_info.single_slice_dim([9, 2]))
partition_info = variable_scope._PartitionInfo(
    full_shape=[9, 3], var_offset=[4, 0])
self.assertEqual(0, partition_info.single_slice_dim([2, 3]))
