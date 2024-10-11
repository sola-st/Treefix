# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
choice = lambda s: np.random.choice((False, True), size=s)
# Nothing to squeeze.
self._compareSqueezeAll(choice([2]))
self._compareSqueezeAll(choice([2, 3]))

# Squeeze the middle element away.
self._compareSqueezeAll(choice([2, 1, 2]))

# Squeeze on both ends.
self._compareSqueezeAll(choice([1, 2, 1, 3, 1]))
