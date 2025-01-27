# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
lam = constant_op.constant([0.1, 1.0])
with backprop.GradientTape() as tape:
    tape.watch(lam)
    exponential = exponential_lib.Exponential(rate=lam)
    samples = exponential.sample(100)
grad_lam = tape.gradient(samples, lam)
self.assertIsNotNone(grad_lam)
