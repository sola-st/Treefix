# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = np.array([[0.2, 0.7], [0.5, 0.4]], dtype=np.float32)
dist = bernoulli.Bernoulli(probs=p)
self.assertAllEqual(self.evaluate(dist.mean()), p)
