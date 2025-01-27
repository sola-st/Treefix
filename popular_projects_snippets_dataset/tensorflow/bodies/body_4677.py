# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
x = constant_op.constant([[1., 2.], [3., 4.]])
x_r = dist.reduce(reduce_util.ReduceOp.SUM, x, axis=None)
self.assertAllEqual(self.evaluate(x), self.evaluate(x_r))
x_r = dist.reduce(reduce_util.ReduceOp.SUM, x, axis=0)
self.assertAllEqual([4., 6.], self.evaluate(x_r))
x_r = dist.reduce(reduce_util.ReduceOp.SUM, x, axis=(0, 1))
self.assertEqual(10., self.evaluate(x_r))
