# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
batch_size = 6
alpha = constant_op.constant([[2.0, 4.0]] * batch_size)
beta = constant_op.constant(3.0)
alpha_v = np.array([2.0, 4.0])
beta_v = 3.0
x = np.array([[2.5, 2.5, 4.0, 0.1, 1.0, 2.0]], dtype=np.float32).T
gamma = gamma_lib.Gamma(concentration=alpha, rate=beta)
log_pdf = gamma.log_prob(x)
log_pdf_values = self.evaluate(log_pdf)
self.assertEqual(log_pdf.get_shape(), (6, 2))
pdf = gamma.prob(x)
pdf_values = self.evaluate(pdf)
self.assertEqual(pdf.get_shape(), (6, 2))

if not stats:
    exit()
expected_log_pdf = stats.gamma.logpdf(x, alpha_v, scale=1 / beta_v)
self.assertAllClose(log_pdf_values, expected_log_pdf)
self.assertAllClose(pdf_values, np.exp(expected_log_pdf))
