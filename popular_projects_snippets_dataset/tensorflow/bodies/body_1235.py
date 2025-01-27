# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
with self.session() as sess, self.test_scope():
    handle = resource_variable_ops.var_handle_op(
        dtype=dtypes.float32, shape=[8])
    sess.run(
        resource_variable_ops.assign_variable_op(
            handle, constant_op.constant([1] * 8, dtype=dtypes.float32)))
    indices = constant_op.constant([[4], [3], [1], [7]], dtype=dtypes.int32)
    updates = constant_op.constant([9, 10, 11, 12], dtype=dtypes.float32)
    expected = np.array([1, 11, 1, 10, 9, 1, 1, 12])
    sess.run(
        gen_state_ops.resource_scatter_nd_update(handle, indices, updates))
    read = resource_variable_ops.read_variable_op(
        handle, dtype=dtypes.float32)
    self.assertAllClose(expected, self.evaluate(read))
