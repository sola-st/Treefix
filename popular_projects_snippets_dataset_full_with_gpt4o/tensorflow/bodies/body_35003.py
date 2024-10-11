# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
# df = 1.5 ==> infinite variance.
df = [1.5, 3., 5., 7.]
mu = [0., 1., 3.3, 4.4]
sigma = [4., 3., 2., 1.]
student = student_t.StudentT(df=df, loc=mu, scale=sigma)
var = self.evaluate(student.variance())

if not stats:
    exit()
expected_var = [
    stats.t.var(d, loc=m, scale=s) for (d, m, s) in zip(df, mu, sigma)
]
self.assertAllClose(expected_var, var)
