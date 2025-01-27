# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha = constant_op.constant(4.0)
beta = constant_op.constant(3.0)
with backprop.GradientTape() as tape:
    tape.watch(alpha)
    tape.watch(beta)
    gamma = gamma_lib.Gamma(concentration=alpha, rate=beta)
    samples = gamma.sample(100)
grad_alpha, grad_beta = tape.gradient(samples, [alpha, beta])
self.assertIsNotNone(grad_alpha)
self.assertIsNotNone(grad_beta)
