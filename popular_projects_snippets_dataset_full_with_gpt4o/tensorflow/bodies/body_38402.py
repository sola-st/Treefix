# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
shape = [2, 3, 4, 2]
for dtype in [dtypes.float32, dtypes.float64]:
    # zero value entry will result NaN gradient if reduction doesn't happen.
    # e.g., `tf.math.reduce_sum([0, 1], axis=[])` so add one to avoid it.
    x = self._makeIncremental(shape, dtype) + 1.0
    self._compareGradientAxes(x, rtol=1e-2, atol=1e-2)
