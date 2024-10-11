# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
weights = np.asarray((5, 11)).reshape((1, 2, 1))
self._test_valid(
    weights=weights,
    values=_test_values((3, 2, 4)),
    expected=np.tile(weights, reps=(3, 1, 4)))
