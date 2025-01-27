# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# Positive squeeze dim index.
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]), [0])
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]), [2, 4])
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]), [0, 4, 2])

# Negative squeeze dim index.
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]), [-1])
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]), [-3, -5])
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]), [-3, -5, -1])
