# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = [0.5, 0.7, 0.3]
for dtype in [np.float32, np.double]:
    # Test scalar and vector versions.
    for denom in [x[0], [x[0]] * 3]:
        x_np = np.array(x, dtype=dtype)
        with test_util.use_gpu():
            x_tf = constant_op.constant(x_np, shape=x_np.shape)
            y_tf = math_ops.mod(x_tf, denom)
            y_tf_np = self.evaluate(y_tf)
            y_np = np.fmod(x_np, denom)
        self.assertAllClose(y_tf_np, y_np, atol=1e-2)
