# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
total_count = constant_op.constant(5.0)
p = constant_op.constant([0.2, 0.6])
with backprop.GradientTape() as tape:
    tape.watch(total_count)
    tape.watch(p)
    dist = multinomial.Multinomial(
        total_count=total_count,
        probs=p)
    samples = dist.sample(100)
grad_total_count, grad_p = tape.gradient(samples, [total_count, p])
self.assertIsNone(grad_total_count)
self.assertIsNone(grad_p)
