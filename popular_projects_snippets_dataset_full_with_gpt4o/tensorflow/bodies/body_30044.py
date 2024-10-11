# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
weights = np.asarray((
    5, 7, 11, 3, 2, 12, 7, 5, 2, 17, 11, 3)).reshape((3, 1, 4))
self._test_valid(
    weights=weights,
    values=_test_values((3, 2, 4)),
    expected=np.tile(weights, reps=(1, 2, 1)))
