# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[4], [3], [1], [7]], dtype=dtypes.int32)
updates = constant_op.constant([False, True, False, True],
                               dtype=dtypes.bool)
expected = np.array([False, False, False, True, False, False, False, True])
scatter = self.scatter_nd(indices, updates, shape=(8,))
result = self.evaluate(scatter)
self.assertAllEqual(expected, result)

# Same indice is updated twice by same value.
indices = constant_op.constant([[4], [3], [3], [7]], dtype=dtypes.int32)
updates = constant_op.constant([False, True, True, True], dtype=dtypes.bool)
expected = np.array([False, False, False, True, False, False, False, True])
scatter = self.scatter_nd(indices, updates, shape=(8,))
result = self.evaluate(scatter)
self.assertAllEqual(expected, result)
