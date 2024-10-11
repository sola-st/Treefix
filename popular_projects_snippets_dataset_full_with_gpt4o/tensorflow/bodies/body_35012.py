# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df = constant_op.constant([-3.2, -4.6])
mu = constant_op.constant([-4.2, 3.4])
sigma = constant_op.constant([-6.4, -8.8])
student = student_t.StudentTWithAbsDfSoftplusScale(
    df=df, loc=mu, scale=sigma)
self.assertAllClose(
    math_ops.floor(self.evaluate(math_ops.abs(df))),
    self.evaluate(student.df))
self.assertAllClose(self.evaluate(mu), self.evaluate(student.loc))
self.assertAllClose(
    self.evaluate(nn_ops.softplus(sigma)), self.evaluate(student.scale))
