# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
batch_size = 6
df = constant_op.constant([[1.5, 7.2]] * batch_size)
mu = constant_op.constant([[3., -3.]] * batch_size)
sigma = constant_op.constant(
    [[-math.sqrt(10.), math.sqrt(15.)]] * batch_size)
df_v = np.array([1.5, 7.2])
mu_v = np.array([3., -3.])
sigma_v = np.array([np.sqrt(10.), np.sqrt(15.)])
t = np.array([[-2.5, 2.5, 4., 0., -1., 2.]], dtype=np.float32).T
student = student_t.StudentT(df, loc=mu, scale=sigma)
log_pdf = student.log_prob(t)
log_pdf_values = self.evaluate(log_pdf)
self.assertEqual(log_pdf.get_shape(), (6, 2))
pdf = student.prob(t)
pdf_values = self.evaluate(pdf)
self.assertEqual(pdf.get_shape(), (6, 2))

if not stats:
    exit()
expected_log_pdf = stats.t.logpdf(t, df_v, loc=mu_v, scale=sigma_v)
expected_pdf = stats.t.pdf(t, df_v, loc=mu_v, scale=sigma_v)
self.assertAllClose(expected_log_pdf, log_pdf_values)
self.assertAllClose(np.log(expected_pdf), log_pdf_values)
self.assertAllClose(expected_pdf, pdf_values)
self.assertAllClose(np.exp(expected_log_pdf), pdf_values)
