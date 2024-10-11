# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
histogram = [0.1, 0.2, 0.3, 0.4]
event = 2
expected_cdf = 0.3
dist = categorical.Categorical(probs=histogram)
cdf_op = dist.cdf(event)

with self.cached_session():
    self.assertAlmostEqual(cdf_op.eval(), expected_cdf)
