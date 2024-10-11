# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df = [0.5, 1., 3]
mu = [-1, 0., 1]
sigma = [5., 4., 3.]
student = student_t.StudentT(df=df, loc=mu, scale=sigma)
# Test broadcast of mu across shape of df/sigma
mode = self.evaluate(student.mode())
self.assertAllClose([-1., 0, 1], mode)
