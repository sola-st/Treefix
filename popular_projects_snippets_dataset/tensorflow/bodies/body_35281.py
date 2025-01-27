# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
histograms = [0.2, 0.8]
dist = categorical.Categorical(math_ops.log(histograms) - 50.)
with self.cached_session():
    self.assertAllClose(dist.prob(0), 0.2)
