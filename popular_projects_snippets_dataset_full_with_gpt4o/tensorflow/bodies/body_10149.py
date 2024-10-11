# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant([[0.], [1.]], dtype=dtype)
    y = constant_op.constant([[0.1, 0.2, 3.5], [0., 1., 2.]], dtype=dtype)
    with test_util.use_gpu():
        xdivy_tf_np = self.evaluate(math_ops.xdivy(x, y))
        zeros_np = self.evaluate(array_ops.zeros_like(y[0]))
        x_over_y = self.evaluate(1 / y[1])
        self.assertAllClose(zeros_np, xdivy_tf_np[0])
        self.assertAllClose(x_over_y, xdivy_tf_np[1])
