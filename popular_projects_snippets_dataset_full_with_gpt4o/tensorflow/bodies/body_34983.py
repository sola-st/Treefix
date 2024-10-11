# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
batch_size = 6
df = constant_op.constant([3.] * batch_size)
mu = constant_op.constant([7.] * batch_size)
sigma = constant_op.constant([8.] * batch_size)
df_v = 3.
mu_v = 7.
sigma_v = 8.
t = np.array([-2.5, 2.5, 8., 0., -1., 2.], dtype=np.float32)
student = student_t.StudentT(df, loc=mu, scale=-sigma)  # pylint: disable=invalid-unary-operand-type

log_pdf = student.log_prob(t)
self.assertEqual(log_pdf.get_shape(), (6,))
log_pdf_values = self.evaluate(log_pdf)
pdf = student.prob(t)
self.assertEqual(pdf.get_shape(), (6,))
pdf_values = self.evaluate(pdf)

if not stats:
    exit()

expected_log_pdf = stats.t.logpdf(t, df_v, loc=mu_v, scale=sigma_v)
expected_pdf = stats.t.pdf(t, df_v, loc=mu_v, scale=sigma_v)
self.assertAllClose(expected_log_pdf, log_pdf_values)
self.assertAllClose(np.log(expected_pdf), log_pdf_values)
self.assertAllClose(expected_pdf, pdf_values)
self.assertAllClose(np.exp(expected_log_pdf), pdf_values)
