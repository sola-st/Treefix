# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df = constant_op.constant(4.)
mu = constant_op.constant(3.)
sigma = constant_op.constant(-math.sqrt(10.))
df_v = 4.
mu_v = 3.
sigma_v = np.sqrt(10.)
n = constant_op.constant(200000)
student = student_t.StudentT(df=df, loc=mu, scale=sigma)
samples = student.sample(n, seed=123456)
sample_values = self.evaluate(samples)
n_val = 200000
self.assertEqual(sample_values.shape, (n_val,))
self.assertAllClose(sample_values.mean(), mu_v, rtol=0.1, atol=0)
self.assertAllClose(
    sample_values.var(), sigma_v**2 * df_v / (df_v - 2), rtol=0.1, atol=0)
self._checkKLApprox(df_v, mu_v, sigma_v, sample_values)
