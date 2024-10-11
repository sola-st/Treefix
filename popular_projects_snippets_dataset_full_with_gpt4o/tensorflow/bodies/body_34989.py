# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df_v = [1e-1, 1e-5, 1e-10, 1e-20]
df = constant_op.constant(df_v)
n = constant_op.constant(200000)
student = student_t.StudentT(df=df, loc=1., scale=1.)
samples = student.sample(n, seed=123456)
sample_values = self.evaluate(samples)
n_val = 200000
self.assertEqual(sample_values.shape, (n_val, 4))
self.assertTrue(np.all(np.logical_not(np.isnan(sample_values))))
