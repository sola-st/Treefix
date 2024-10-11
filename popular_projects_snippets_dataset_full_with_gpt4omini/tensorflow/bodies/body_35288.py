# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
logits = np.log([[0.2, 0.8], [0.6, 0.4]]) - 50.
dist = categorical.Categorical(logits)
with self.cached_session():
    self.assertAllClose(dist.log_prob([0, 1]), np.log([0.2, 0.4]))
    self.assertAllClose(dist.log_prob([0.0, 1.0]), np.log([0.2, 0.4]))
