# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session():
    histograms = [[[0.2, 0.8], [0.6, 0.4]]]
    dist = categorical.Categorical(math_ops.log(histograms) - 50.)
    self.assertAllEqual(dist.mode(), [[1, 0]])
