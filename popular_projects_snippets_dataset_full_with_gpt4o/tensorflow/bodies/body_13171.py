# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
np.random.seed(0)
x_init = np.random.randn(batch_size, dimensions).astype(dtype)
with self.cached_session():
    x = array_ops.placeholder(dtype, (batch_size, dimensions))
    y, _ = nn_ops.isotonic_regression(x)  # Segments have no gradient.
    max_error = gradient_checker.compute_gradient_error(
        x, (batch_size, dimensions), y, (batch_size, dimensions), x_init)
self.assertAllClose(max_error, 0.)
