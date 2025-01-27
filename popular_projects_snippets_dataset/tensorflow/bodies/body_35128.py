# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
batch_size = 6
alpha = constant_op.constant([2.0] * batch_size)
beta = constant_op.constant([3.0] * batch_size)
alpha_v = 2.0
beta_v = 3.0
x = np.array([2.5, 2.5, 4.0, 0.1, 1.0, 2.0], dtype=np.float32)
gamma = gamma_lib.Gamma(concentration=alpha, rate=beta)
log_pdf = gamma.log_prob(x)
self.assertEqual(log_pdf.get_shape(), (6,))
pdf = gamma.prob(x)
self.assertEqual(pdf.get_shape(), (6,))
if not stats:
    exit()
expected_log_pdf = stats.gamma.logpdf(x, alpha_v, scale=1 / beta_v)
self.assertAllClose(self.evaluate(log_pdf), expected_log_pdf)
self.assertAllClose(self.evaluate(pdf), np.exp(expected_log_pdf))
