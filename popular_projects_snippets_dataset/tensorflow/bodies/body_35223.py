# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = constant_op.constant([1.0, 2.0, 3.0])
with backprop.GradientTape() as tape:
    tape.watch(alpha)
    dirichlet = dirichlet_lib.Dirichlet(alpha)
    samples = dirichlet.sample(100)
grad_alpha = tape.gradient(samples, alpha)
self.assertIsNotNone(grad_alpha)
