# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
self.assertAllEqual(a.indices, b.indices)
self.assertAllEqual(a.values, b.values)
self.assertAllEqual(a.dense_shape, b.dense_shape)
