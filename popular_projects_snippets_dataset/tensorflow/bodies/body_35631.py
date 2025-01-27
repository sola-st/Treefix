# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
sample = random_ops.random_poisson(shape=[2], lam=np.inf)
self.assertAllEqual([np.inf, np.inf], self.evaluate(sample))
