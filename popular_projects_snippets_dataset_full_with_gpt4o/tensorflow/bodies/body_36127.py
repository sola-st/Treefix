# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v = resource_variable_ops.ResourceVariable(
        [1, 2, 3, 4, 5, 6, 7, 8], dtype=dtypes.float32, name="sub")
    indices = constant_op.constant([[4], [3], [1], [7]], dtype=dtypes.int32)
    updates = constant_op.constant([9, 10, 11, 12], dtype=dtypes.float32)
    expected = np.array([1, -9, 3, -6, -4, 6, 7, -4])
    state_ops.scatter_nd_sub(v, indices, updates)
    self.assertAllClose(expected, v.numpy())
