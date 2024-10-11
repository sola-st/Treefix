# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
self.assertAllEqual(expected.values, result.values, msg='Values differ')
self.assertAllEqual(
    expected.indices, result.indices, msg='Indices differ')
self.assertAllEqual(
    expected.dense_shape, result.dense_shape, msg='Shapes differ')
