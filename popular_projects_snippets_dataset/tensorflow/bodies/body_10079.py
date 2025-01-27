# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in [np.float16, np.float32, np.double]:
    x_np = np.random.rand(5, 5).astype(dtype)
    with test_util.use_gpu():
        y_tf = math_ops.reduce_logsumexp(x_np, axis=0)
        y_np = np.log(np.sum(np.exp(x_np), axis=0))
        self.assertShapeEqual(y_np, y_tf)
        y_tf_np = self.evaluate(y_tf)
        self.assertAllClose(y_tf_np, y_np)
