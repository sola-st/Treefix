# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant([[0.1, 0.2, 3.5], [-2., -5., 30.]], dtype=dtype)
    y = constant_op.constant([[0.1, 0.2, 3.5], [3.1, 4., 2.]], dtype=dtype)
    with test_util.use_gpu():
        xdivy = self.evaluate(math_ops.xdivy(x, y))
        x_over_y = self.evaluate(x / y)
        self.assertAllClose(xdivy, x_over_y)
