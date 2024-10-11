# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = constant_op.constant([0.2, 0.6])
with backprop.GradientTape() as tape:
    tape.watch(p)
    dist = bernoulli.Bernoulli(probs=p)
    samples = dist.sample(100)
grad_p = tape.gradient(samples, p)
self.assertIsNone(grad_p)
