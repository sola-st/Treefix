# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
mu = [-2, 0., 1., 3.3, 4.4]
sigma = [5., 4., 3., 2., 1.]
student = student_t.StudentT(
    df=[0.5, 1., 3., 5., 7.], loc=mu, scale=sigma, allow_nan_stats=True)
mean = self.evaluate(student.mean())
self.assertAllClose([np.nan, np.nan, 1., 3.3, 4.4], mean)
