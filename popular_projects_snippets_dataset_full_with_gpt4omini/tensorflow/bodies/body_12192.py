# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops_test.py
self._testNonFiniteClippingByGlobalNorm(
    [[-3.0, 0.0, 0.0], [float("inf"), 0.0, 0.0]], 4.0)
self._testNonFiniteClippingByGlobalNorm(
    [[-3.0, 0.0, 0.0], [float("-inf"), 0.0, 0.0]], 4.0)
self._testNonFiniteClippingByGlobalNorm(
    [[-3.0, 0.0, 0.0], [float("nan"), 0.0, 0.0]], 4.0)
