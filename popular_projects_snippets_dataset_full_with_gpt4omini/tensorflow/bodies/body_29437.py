# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[1]], dtype=dtypes.int32)
updates = constant_op.constant([[11., 12.]], dtype=dtypes.float32)
ref = variables.Variable([[0., 0.], [0., 0.], [0., 0.]],
                         dtype=dtypes.float32)
expected = np.array([[0., 0.], [11., 12.], [0., 0.]])
scatter = state_ops.scatter_nd_update(ref, indices, updates)
init = variables.global_variables_initializer()

with self.session():
    self.evaluate(init)
    result = self.evaluate(scatter)
    self.assertAllClose(result, expected)
