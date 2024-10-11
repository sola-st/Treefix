# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
self.assertEqual(0, sp.indices.size)
self.assertEqual(0, sp.values.size)
# TODO(zakaria): check if we can ignore the first dim of the shape.
self.assertEqual(0, sp.dense_shape[1])
