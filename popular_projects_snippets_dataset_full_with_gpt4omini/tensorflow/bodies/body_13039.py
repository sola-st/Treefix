# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [20, 7, 3]
np.random.seed(1)  # Make it reproducible.
x_val = np.random.random_sample(x_shape).astype(np.float64)
with self.cached_session():
    x = constant_op.constant(x_val, name="x")
    theoretical, numerical = gradient_checker_v2.compute_gradient(
        nn_ops.l2_loss, [x])
    self.assertAllClose(theoretical, numerical)
