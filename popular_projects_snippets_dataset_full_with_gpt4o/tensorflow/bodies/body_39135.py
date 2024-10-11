# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
self.assertAllEqual(sp1.indices, sp2.indices)
self.assertAllEqual(sp1.values, sp2.values)
self.assertAllEqual(sp1.dense_shape, sp2.dense_shape)
