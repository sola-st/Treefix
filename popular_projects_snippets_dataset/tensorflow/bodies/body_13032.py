# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [5, 10]
x_np = np.random.randn(*x_shape).astype(np.float32)
z_np = np.random.randint(0, 5, size=x_shape).astype(np.float32)
y_np = self._log_poisson_loss(x_np, z_np, compute_full_loss=False)
y_np_stirling = self._log_poisson_loss(x_np, z_np, compute_full_loss=True)
y_tf = nn_impl.log_poisson_loss(z_np, x_np, compute_full_loss=False)
y_tf_stirling = nn_impl.log_poisson_loss(z_np, x_np, compute_full_loss=True)
y_tf_np = self.evaluate(y_tf)
y_tf_np_stirling = self.evaluate(y_tf_stirling)
eps = 1e-3
self.assertAllClose(y_tf_np, y_np, eps)
self.assertAllClose(y_tf_np_stirling, y_np_stirling, eps)
