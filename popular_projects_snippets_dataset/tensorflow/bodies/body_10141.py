# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant([[0.1, 0.2, 3.5], [-2., -5., 30.]], dtype=dtype)
    y = constant_op.constant([[0.1, 0.2, 3.5], [3.1, 4., 2.]], dtype=dtype)
    with test_util.use_gpu():
        xlogy = self.evaluate(math_ops.xlogy(x, y))
        xtimeslogy = self.evaluate(x * math_ops.log(y))
        self.assertAllClose(xlogy, xtimeslogy)
