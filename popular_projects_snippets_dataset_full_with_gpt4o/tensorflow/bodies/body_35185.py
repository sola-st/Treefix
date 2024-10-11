# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
batch_size = 6
loc = constant_op.constant([[2.0, 4.0]] * batch_size)
scale = constant_op.constant(3.0)
loc_v = np.array([2.0, 4.0])
scale_v = 3.0
x = np.array([[2.5, 2.5, 4.0, 0.1, 1.0, 2.0]], dtype=np.float32).T
laplace = laplace_lib.Laplace(loc=loc, scale=scale)
log_pdf = laplace.log_prob(x)
log_pdf_values = self.evaluate(log_pdf)
self.assertEqual(log_pdf.get_shape(), (6, 2))

pdf = laplace.prob(x)
pdf_values = self.evaluate(pdf)
self.assertEqual(pdf.get_shape(), (6, 2))
if not stats:
    exit()
expected_log_pdf = stats.laplace.logpdf(x, loc_v, scale=scale_v)
self.assertAllClose(log_pdf_values, expected_log_pdf)
self.assertAllClose(pdf_values, np.exp(expected_log_pdf))
