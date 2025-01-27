# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Invalid arg types.
with self.assertRaises(TypeError):
    variable_scope._PartitionInfo(full_shape=None, var_offset=[0, 1])
with self.assertRaises(TypeError):
    variable_scope._PartitionInfo(full_shape=[0, 1], var_offset=None)
with self.assertRaises(TypeError):
    variable_scope._PartitionInfo(full_shape="foo", var_offset=[0, 1])
with self.assertRaises(TypeError):
    variable_scope._PartitionInfo(full_shape=[0, 1], var_offset="foo")

# full_shape and var_offset must have same length.
with self.assertRaises(ValueError):
    variable_scope._PartitionInfo(full_shape=[0, 1], var_offset=[0])
# Offset must always be less than shape.
with self.assertRaises(ValueError):
    variable_scope._PartitionInfo(full_shape=[1, 1], var_offset=[0, 1])
