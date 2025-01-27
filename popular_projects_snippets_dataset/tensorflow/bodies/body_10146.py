# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant([[0.], [1.]], dtype=dtype)
    y = constant_op.constant([[-0.1, -0.2, -1.], [0., 1., 2.]], dtype=dtype)
    with test_util.use_gpu():
        xlog1py_tf_np = self.evaluate(math_ops.xlog1py(x, y))
        zeros_np = self.evaluate(array_ops.zeros_like(y[0]))
        xtimes_log1py = self.evaluate(math_ops.log1p(y[1]))
        self.assertAllClose(zeros_np, xlog1py_tf_np[0])
        self.assertAllClose(xtimes_log1py, xlog1py_tf_np[1])
