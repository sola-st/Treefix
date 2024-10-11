# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/weights_broadcast_test.py
self._test_valid(
    weights=np.asarray((5,)).reshape((1, 1, 1)),
    values=_test_values((3, 2, 4)))
