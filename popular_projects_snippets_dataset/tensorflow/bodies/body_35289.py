# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
logits = np.log([0.2, 0.8]) - 50.
dist = categorical.Categorical(logits)
with self.cached_session():
    self.assertAllClose(dist.entropy(),
                        -(0.2 * np.log(0.2) + 0.8 * np.log(0.8)))
