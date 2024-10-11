# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = np.arange(-5.0, 5.0, .25)
for dtype in [np.float32, np.double, np.int32]:
    x_np = np.array(x, dtype=dtype)
    with test_util.device(use_gpu=True):
        x_tf = constant_op.constant(x_np, shape=x_np.shape)
        y_tf = math_ops.round(x_tf)
        y_tf_np = self.evaluate(y_tf)
        y_np = np.round(x_np)
        self.assertAllClose(y_tf_np, y_np, atol=1e-2)
