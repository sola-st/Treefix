# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
t_value = [[0, 42], [24, 0]]
self.assertAllEqual((2, 2), self.evaluate(array_ops.shape(t_value)))
self.assertEqual(4, self.evaluate(array_ops.size(t_value)))
self.assertEqual(2, self.evaluate(array_ops.rank(t_value)))

t = constant_op.constant(t_value)
self.assertAllEqual((2, 2), self.evaluate(array_ops.shape(t)))
self.assertEqual(4, self.evaluate(array_ops.size(t)))
self.assertEqual(2, self.evaluate(array_ops.rank(t)))
