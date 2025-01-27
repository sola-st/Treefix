# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
batch_size = 6
df = constant_op.constant([3.] * batch_size)
mu = constant_op.constant([7.] * batch_size)
sigma = constant_op.constant([-8.] * batch_size)
df_v = 3.
mu_v = 7.
sigma_v = 8.
t = np.array([-2.5, 2.5, 8., 0., -1., 2.], dtype=np.float32)
student = student_t.StudentT(df, loc=mu, scale=sigma)

log_cdf = student.log_cdf(t)
self.assertEqual(log_cdf.get_shape(), (6,))
log_cdf_values = self.evaluate(log_cdf)
cdf = student.cdf(t)
self.assertEqual(cdf.get_shape(), (6,))
cdf_values = self.evaluate(cdf)

if not stats:
    exit()
expected_log_cdf = stats.t.logcdf(t, df_v, loc=mu_v, scale=sigma_v)
expected_cdf = stats.t.cdf(t, df_v, loc=mu_v, scale=sigma_v)
self.assertAllClose(expected_log_cdf, log_cdf_values, atol=0., rtol=1e-5)
self.assertAllClose(
    np.log(expected_cdf), log_cdf_values, atol=0., rtol=1e-5)
self.assertAllClose(expected_cdf, cdf_values, atol=0., rtol=1e-5)
self.assertAllClose(
    np.exp(expected_log_cdf), cdf_values, atol=0., rtol=1e-5)
