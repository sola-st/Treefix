# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = [-1000, -1001, -1002, -1003]
for dtype in [np.float16, np.float32, np.double]:
    x_np = np.array(x, dtype=dtype)
    max_np = np.max(x_np)
    with self.assertRaisesRegex(RuntimeWarning,
                                "divide by zero encountered in log"):
        out = np.log(np.sum(np.exp(x_np)))
        if out == -np.inf:
            raise RuntimeWarning("divide by zero encountered in log")

    with test_util.use_gpu():
        x_tf = constant_op.constant(x_np, shape=x_np.shape)
        y_tf_np = math_ops.reduce_logsumexp(x_tf)
        y_np = np.log(np.sum(np.exp(x_np - max_np))) + max_np
        self.assertAllClose(y_tf_np, y_np)
