# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [5, 10]
x_np = np.random.randn(*x_shape).astype(np.float64)
z_np = np.random.randint(0, 5, size=x_shape).astype(np.float64)
with self.cached_session():
    x_tf = constant_op.constant(x_np)
    # TODO(b/241834841): Test with `compute_full_loss` set as True
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        nn_impl.log_poisson_loss, [z_np, x_tf])
    self.assertAllClose(theoretical, numerical)
