# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
p = constant_op.constant([0.3, 0.3, 0.4])
with backprop.GradientTape() as tape:
    tape.watch(p)
    dist = categorical.Categorical(p)
    samples = dist.sample(100)
grad_p = tape.gradient(samples, p)
self.assertIsNone(grad_p)
