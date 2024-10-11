# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = constant_op.constant(1.0)
b = constant_op.constant(2.0)
with backprop.GradientTape() as tape:
    tape.watch(a)
    tape.watch(b)
    beta = beta_lib.Beta(a, b)
    samples = beta.sample(100)
grad_a, grad_b = tape.gradient(samples, [a, b])
self.assertIsNotNone(grad_a)
self.assertIsNotNone(grad_b)
