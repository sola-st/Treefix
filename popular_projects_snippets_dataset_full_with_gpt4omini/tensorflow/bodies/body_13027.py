# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [5, 10]
x_np = np.random.randn(*x_shape).astype(np.float32)
y_np = self._softmax(x_np)
x_tf = constant_op.constant(x_np)
y_tf = nn_ops.softmax_v2(x_tf)
y_tf_last_dim = nn_ops.softmax_v2(x_tf, 1)
y_tf_np = self.evaluate(y_tf)
y_tf_last_dim_np = self.evaluate(y_tf_last_dim)
eps = 1e-3
self.assertAllClose(y_tf_np, y_np, eps)
self.assertAllClose(y_tf_last_dim_np, y_np, eps)
