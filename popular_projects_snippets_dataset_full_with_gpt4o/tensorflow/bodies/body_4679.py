# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
x = constant_op.constant(1.)
x_r = dist.extended.reduce_to(reduce_util.ReduceOp.MEAN, x, "/CPU:0")
self.assertEqual(self.evaluate(x), self.evaluate(x_r))
