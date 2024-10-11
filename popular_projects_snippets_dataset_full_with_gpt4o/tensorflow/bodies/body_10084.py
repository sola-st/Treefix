# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.double]:
    x_rt = ragged_factory_ops.constant([[1, 2], [], [3, 4, 5]], dtype=dtype)
    x_np = np.array(self.evaluate(x_rt.flat_values))
    with test_util.use_gpu():
        y_rt = math_ops.reduce_logsumexp(x_rt)
        y_np = np.log(np.sum(np.exp(x_np - np.max(x_np)))) + np.max(x_np)
        self.assertAllClose(y_rt, y_np)
