# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc_v = constant_op.constant([0.0, 1.0], name="loc")
scale_v = constant_op.constant([-1.0, 2.0], name="scale")
laplace = laplace_lib.LaplaceWithSoftplusScale(loc=loc_v, scale=scale_v)
self.assertAllClose(
    self.evaluate(nn_ops.softplus(scale_v)), self.evaluate(laplace.scale))
self.assertAllClose(self.evaluate(loc_v), self.evaluate(laplace.loc))
