# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
total_count = constant_op.constant(5.0)
concentration = constant_op.constant([0.1, 0.1, 0.1])
with backprop.GradientTape() as tape:
    tape.watch(total_count)
    tape.watch(concentration)
    dist = ds.DirichletMultinomial(
        total_count=total_count,
        concentration=concentration)
    samples = dist.sample(100)
grad_total_count, grad_concentration = tape.gradient(
    samples, [total_count, concentration])
self.assertIsNone(grad_total_count)
self.assertIsNone(grad_concentration)
