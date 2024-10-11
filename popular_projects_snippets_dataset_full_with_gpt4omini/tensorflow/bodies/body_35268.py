# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
mu = constant_op.constant(4.0)
sigma = constant_op.constant(3.0)
with backprop.GradientTape() as tape:
    tape.watch(mu)
    tape.watch(sigma)
    normal = normal_lib.Normal(loc=mu, scale=sigma)
    samples = normal.sample(100)
grad_mu, grad_sigma = tape.gradient(samples, [mu, sigma])
self.assertIsNotNone(grad_mu)
self.assertIsNotNone(grad_sigma)
