# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
lam_v = np.array([1.0, 4.0, 2.5])
exponential = exponential_lib.Exponential(rate=lam_v)
self.assertEqual(exponential.variance().get_shape(), (3,))
if not stats:
    exit()
expected_variance = stats.expon.var(scale=1 / lam_v)
self.assertAllClose(
    self.evaluate(exponential.variance()), expected_variance)
