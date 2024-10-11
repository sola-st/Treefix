# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x1l, x2l = zip((+0.0, +0.0), (+0.0, -0.0), (-0.0, +0.0), (-0.0, -0.0),
               (1.0, 0.0), (-1.0, 0.0), (1.0, -0.0), (-1.0, -0.0),
               (0.0, 1.0), (0.0, -1.0), (-0.0, 1.0), (-0.0, -1.0),
               (1.2345, float("inf")), (1.2345, -float("inf")),
               (-4.321, float("inf")), (-4.125, -float("inf")),
               (float("inf"), float("inf")), (float("inf"), -float("inf")),
               (-float("inf"), float("inf")),
               (-float("inf"), -float("inf")), (float("1"), float("nan")),
               (float("nan"), float("1")), (float("nan"), float("nan")))
for dtype in np.float32, np.float64:
    x1 = np.array(x1l).astype(dtype)
    x2 = np.array(x2l).astype(dtype)
    self._compareCpu(x1, x2, np.arctan2, math_ops.atan2)
    self._compareGpu(x1, x2, np.arctan2, math_ops.atan2)
