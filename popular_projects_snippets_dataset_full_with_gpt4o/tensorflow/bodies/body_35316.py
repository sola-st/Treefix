# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = 10.0
b = [11.0, 100.0]
uniform = uniform_lib.Uniform(low=a, high=b)

no_nans = constant_op.constant(1.0)
nans = constant_op.constant(0.0) / constant_op.constant(0.0)
self.assertTrue(self.evaluate(math_ops.is_nan(nans)))
with_nans = array_ops.stack([no_nans, nans])

pdf = uniform.prob(with_nans)

is_nan = self.evaluate(math_ops.is_nan(pdf))
self.assertFalse(is_nan[0])
self.assertTrue(is_nan[1])
