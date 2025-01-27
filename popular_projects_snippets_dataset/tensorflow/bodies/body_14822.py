# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random_test.py
low = np.zeros(low_shape).astype(np.float64)
high = np.ones(high_shape).astype(np.float64)
self._test(low=low, high=high, size=size)
