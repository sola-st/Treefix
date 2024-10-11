# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
df = constant_op.constant(2.0)
mu = constant_op.constant(1.0)
sigma = constant_op.constant(3.0)
with backprop.GradientTape() as tape:
    tape.watch(df)
    tape.watch(mu)
    tape.watch(sigma)
    student = student_t.StudentT(df=df, loc=mu, scale=sigma)
    samples = student.sample(100)
grad_df, grad_mu, grad_sigma = tape.gradient(samples, [df, mu, sigma])
self.assertIsNotNone(grad_df)
self.assertIsNotNone(grad_mu)
self.assertIsNotNone(grad_sigma)
