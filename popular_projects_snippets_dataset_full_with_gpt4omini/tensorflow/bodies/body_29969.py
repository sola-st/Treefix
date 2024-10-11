# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
c = constant_op.constant(12, shape=[7])
self.assertEqual(c.get_shape(), [7])
self.assertAllEqual([12, 12, 12, 12, 12, 12, 12], c.numpy())
