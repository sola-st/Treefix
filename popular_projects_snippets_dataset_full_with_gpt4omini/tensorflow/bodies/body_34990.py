# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
batch_size = 7
df = constant_op.constant([[5., 7.]] * batch_size)
mu = constant_op.constant([[3., -3.]] * batch_size)
sigma = constant_op.constant(
    [[math.sqrt(10.), math.sqrt(15.)]] * batch_size)
df_v = [5., 7.]
mu_v = [3., -3.]
sigma_v = [np.sqrt(10.), np.sqrt(15.)]
n = constant_op.constant(200000)
student = student_t.StudentT(df=df, loc=mu, scale=sigma)
samples = student.sample(n, seed=123456)
sample_values = self.evaluate(samples)
self.assertEqual(samples.get_shape(), (200000, batch_size, 2))
self.assertAllClose(
    sample_values[:, 0, 0].mean(), mu_v[0], rtol=0.1, atol=0)
self.assertAllClose(
    sample_values[:, 0, 0].var(),
    sigma_v[0]**2 * df_v[0] / (df_v[0] - 2),
    rtol=0.2,
    atol=0)
self._checkKLApprox(df_v[0], mu_v[0], sigma_v[0], sample_values[:, 0, 0])
self.assertAllClose(
    sample_values[:, 0, 1].mean(), mu_v[1], rtol=0.1, atol=0)
self.assertAllClose(
    sample_values[:, 0, 1].var(),
    sigma_v[1]**2 * df_v[1] / (df_v[1] - 2),
    rtol=0.2,
    atol=0)
self._checkKLApprox(df_v[1], mu_v[1], sigma_v[1], sample_values[:, 0, 1])
