# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
self.evaluate(random_ops.random_gamma(
    [5], alpha=np.ones([2, 1, 3]), beta=np.ones([3]), dtype=np.float32))
