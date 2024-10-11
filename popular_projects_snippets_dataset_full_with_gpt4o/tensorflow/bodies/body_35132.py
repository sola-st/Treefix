# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
batch_size = 6
alpha = constant_op.constant([2.0] * batch_size)
beta = constant_op.constant([3.0] * batch_size)
alpha_v = 2.0
beta_v = 3.0
x = np.array([2.5, 2.5, 4.0, 0.1, 1.0, 2.0], dtype=np.float32)

gamma = gamma_lib.Gamma(concentration=alpha, rate=beta)
cdf = gamma.cdf(x)
self.assertEqual(cdf.get_shape(), (6,))
if not stats:
    exit()
expected_cdf = stats.gamma.cdf(x, alpha_v, scale=1 / beta_v)
self.assertAllClose(self.evaluate(cdf), expected_cdf)
