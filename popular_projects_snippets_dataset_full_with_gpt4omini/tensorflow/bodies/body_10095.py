# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = [5, 10, 23]
for dtype in [np.int32, np.int64]:
    # Test scalar and vector versions.
    for denom in [x[0], x]:
        x_np = np.array(x, dtype=dtype)
        with test_util.use_gpu():
            x_tf = constant_op.constant(x_np, shape=x_np.shape)
            y_tf = math_ops.mod(x_tf, denom)
            y_tf_np = self.evaluate(y_tf)
            y_np = np.mod(x_np, denom)
        self.assertAllClose(y_tf_np, y_np)
