# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# Nothing to squeeze.
self._compareSqueezeAll(np.zeros([2]))
self._compareSqueezeAll(np.zeros([2, 3]))

# Squeeze the middle element away.
self._compareSqueezeAll(np.zeros([2, 1, 2]))

# Squeeze on both ends.
self._compareSqueezeAll(np.zeros([1, 2, 1, 3, 1]))
