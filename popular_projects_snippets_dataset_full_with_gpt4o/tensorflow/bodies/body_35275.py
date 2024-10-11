# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
p = [0.2, 0.8]
dist = categorical.Categorical(probs=p)
with self.cached_session():
    self.assertAllClose(p, dist.probs)
    self.assertAllEqual([2], dist.logits.get_shape())
