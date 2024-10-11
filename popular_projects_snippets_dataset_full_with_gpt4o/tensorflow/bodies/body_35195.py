# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc = constant_op.constant(4.0)
scale = constant_op.constant(3.0)
with backprop.GradientTape() as tape:
    tape.watch(loc)
    tape.watch(scale)
    laplace = laplace_lib.Laplace(loc=loc, scale=scale)
    samples = laplace.sample(100)
grad_loc, grad_scale = tape.gradient(samples, [loc, scale])
self.assertIsNotNone(grad_loc)
self.assertIsNotNone(grad_scale)
