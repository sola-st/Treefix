# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
batch_size = 6
lam = constant_op.constant([2.0] * batch_size)
lam_v = 2.0
x = np.array([2.5, 2.5, 4.0, 0.1, 1.0, 2.0], dtype=np.float32)

exponential = exponential_lib.Exponential(rate=lam)

cdf = exponential.cdf(x)
self.assertEqual(cdf.get_shape(), (6,))

if not stats:
    exit()
expected_cdf = stats.expon.cdf(x, scale=1 / lam_v)
self.assertAllClose(self.evaluate(cdf), expected_cdf)
