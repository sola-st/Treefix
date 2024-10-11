# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([1, 1, 2], dtypes.int32)
updates = array_ops.zeros([1, 1], dtypes.int32)
shape = np.array([2, 2])
ref = variables.Variable(array_ops.zeros(shape, dtypes.int32))
scatter_update = state_ops.scatter_nd_update(ref, indices, updates)
self.assertAllEqual(scatter_update.get_shape().as_list(), shape)

expected_result = np.zeros([2, 2], dtype=np.int32)
with self.cached_session():
    self.evaluate(ref.initializer)
    self.assertAllEqual(expected_result, self.evaluate(scatter_update))
