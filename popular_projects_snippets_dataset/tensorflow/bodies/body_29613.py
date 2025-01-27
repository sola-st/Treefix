# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
a = constant_op.constant([[1, 2, 3], [4, 5, 6]], name='a')
unstacked = self.evaluate(array_ops.unstack(a))

self.assertEqual(len(unstacked), 2)
self.assertAllEqual(unstacked[0], [1, 2, 3])
self.assertAllEqual(unstacked[1], [4, 5, 6])
