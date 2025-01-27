# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session():
    histograms = [[[0.2, 0.8], [0.4, 0.6]]]
    dist = categorical.Categorical(math_ops.log(histograms) - 50.)
    samples = dist.sample((100, 100), seed=123)
    prob = dist.prob(samples)
    prob_val = self.evaluate(prob)
    self.assertAllClose(
        [0.2**2 + 0.8**2], [prob_val[:, :, :, 0].mean()], atol=1e-2)
    self.assertAllClose(
        [0.4**2 + 0.6**2], [prob_val[:, :, :, 1].mean()], atol=1e-2)
