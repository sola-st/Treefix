# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [5, 10]
x_np = np.random.randn(*x_shape).astype(np.float32)
y_np = self._log_softmax(x_np)
x_tf = constant_op.constant(x_np)
y_tf = nn_ops.log_softmax_v2(x_tf)
y_tf_np = self.evaluate(y_tf)
eps = 1e-3
self.assertAllClose(y_tf_np, y_np, eps)
