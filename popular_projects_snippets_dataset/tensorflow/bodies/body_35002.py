# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
# df = 0.5 ==> undefined mean ==> undefined variance.
# df = 1.5 ==> infinite variance.
df = [0.5, 1.5, 3., 5., 7.]
mu = [-2, 0., 1., 3.3, 4.4]
sigma = [5., 4., 3., 2., 1.]
student = student_t.StudentT(
    df=df, loc=mu, scale=sigma, allow_nan_stats=True)
var = self.evaluate(student.variance())

if not stats:
    exit()
expected_var = [
    stats.t.var(d, loc=m, scale=s) for (d, m, s) in zip(df, mu, sigma)
]
# Slicing off first element due to nan/inf mismatch in different SciPy
# versions.
self.assertAllClose(expected_var[1:], var[1:])
