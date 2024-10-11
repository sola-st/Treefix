# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
p = np.array([0.2, 0.8], dtype=np.float32)
logits = np.log(p) - 50.
dist = categorical.Categorical(logits=logits)
with self.cached_session():
    self.assertAllEqual([2], dist.probs.get_shape())
    self.assertAllEqual([2], dist.logits.get_shape())
    self.assertAllClose(dist.probs, p)
    self.assertAllClose(dist.logits, logits)
