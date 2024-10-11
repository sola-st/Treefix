# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([1, 1, 2], dtypes.int32)
updates = array_ops.zeros([1, 1], dtypes.int32)
shape = np.array([2, 2])
scatter = self.scatter_nd(indices, updates, shape)
self.assertAllEqual(scatter.get_shape().as_list(), shape)
expected_result = np.zeros([2, 2], dtype=np.int32)
self.assertAllEqual(expected_result, self.evaluate(scatter))
