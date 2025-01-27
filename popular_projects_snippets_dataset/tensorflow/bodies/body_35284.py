# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
histograms = [[0.1, 0.2, 0.3, 0.25, 0.15],
              [0.0, 0.75, 0.2, 0.05, 0.0]]
event = [0, 3]
expected_cdf = [0.0, 0.95]
dist = categorical.Categorical(probs=histograms)
cdf_op = dist.cdf(event)

with self.cached_session():
    self.assertAllClose(cdf_op, expected_cdf)
