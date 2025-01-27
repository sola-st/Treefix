# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/uniform_test.py
a = constant_op.constant(0.1)
b = constant_op.constant(0.8)
with backprop.GradientTape() as tape:
    tape.watch(a)
    tape.watch(b)
    uniform = uniform_lib.Uniform(a, b)
    samples = uniform.sample(100)
grad_a, grad_b = tape.gradient(samples, [a, b])
self.assertIsNotNone(grad_a)
self.assertIsNotNone(grad_b)
