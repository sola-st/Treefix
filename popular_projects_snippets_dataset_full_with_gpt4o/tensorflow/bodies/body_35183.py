# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
batch_size = 6
loc = constant_op.constant([2.0] * batch_size)
scale = constant_op.constant([3.0] * batch_size)
loc_v = 2.0
scale_v = 3.0
x = np.array([2.5, 2.5, 4.0, 0.1, 1.0, 2.0], dtype=np.float32)
laplace = laplace_lib.Laplace(loc=loc, scale=scale)
log_pdf = laplace.log_prob(x)
self.assertEqual(log_pdf.get_shape(), (6,))
if not stats:
    exit()
expected_log_pdf = stats.laplace.logpdf(x, loc_v, scale=scale_v)
self.assertAllClose(self.evaluate(log_pdf), expected_log_pdf)

pdf = laplace.prob(x)
self.assertEqual(pdf.get_shape(), (6,))
self.assertAllClose(self.evaluate(pdf), np.exp(expected_log_pdf))
