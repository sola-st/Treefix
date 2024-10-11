# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
# Defined for all batch members.
df = [3.5, 5., 3., 5., 7.]
mu = [-2.2]
sigma = [5., 4., 3., 2., 1.]
student = student_t.StudentT(df=df, loc=mu, scale=sigma)
# Test broadcast of mu across shape of df/sigma
stddev = self.evaluate(student.stddev())
mu *= len(df)

if not stats:
    exit()
expected_stddev = [
    stats.t.std(d, loc=m, scale=s) for (d, m, s) in zip(df, mu, sigma)
]
self.assertAllClose(expected_stddev, stddev)
