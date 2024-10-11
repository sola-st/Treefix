# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df_v = np.array([[2., 3., 7.]])  # 1x3
mu_v = np.array([[1., -1, 0]])  # 1x3
sigma_v = np.array([[1., -2., 3.]]).T  # transposed => 3x1
student = student_t.StudentT(df=df_v, loc=mu_v, scale=sigma_v)
ent = student.entropy()
ent_values = self.evaluate(ent)

# Help scipy broadcast to 3x3
ones = np.array([[1, 1, 1]])
sigma_bc = np.abs(sigma_v) * ones
mu_bc = ones.T * mu_v
df_bc = ones.T * df_v
if not stats:
    exit()
expected_entropy = stats.t.entropy(
    np.reshape(df_bc, [-1]),
    loc=np.reshape(mu_bc, [-1]),
    scale=np.reshape(sigma_bc, [-1]))
expected_entropy = np.reshape(expected_entropy, df_bc.shape)
self.assertAllClose(expected_entropy, ent_values)
