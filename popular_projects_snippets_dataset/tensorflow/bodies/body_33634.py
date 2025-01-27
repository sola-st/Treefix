# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
self._test_3d_weighted(
    _test_values((3, 2, 4)),
    weights=np.asarray((5, 7, 11, 3, 2, 13, 7, 5)).reshape((1, 2, 4)))
