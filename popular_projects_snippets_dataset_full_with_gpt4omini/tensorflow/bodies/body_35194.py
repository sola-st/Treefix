# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc_v = 4.0
scale_v = 3.0
loc = constant_op.constant(loc_v)
scale = constant_op.constant(scale_v)
n = 100000
laplace = laplace_lib.Laplace(loc=loc, scale=scale)
samples = laplace.sample(n, seed=137)
sample_values = self.evaluate(samples)
self.assertEqual(samples.get_shape(), (n,))
self.assertEqual(sample_values.shape, (n,))
if not stats:
    exit()
self.assertAllClose(
    sample_values.mean(),
    stats.laplace.mean(loc_v, scale=scale_v),
    rtol=0.05,
    atol=0.)
self.assertAllClose(
    sample_values.var(),
    stats.laplace.var(loc_v, scale=scale_v),
    rtol=0.05,
    atol=0.)
self.assertTrue(self._kstest(loc_v, scale_v, sample_values))
