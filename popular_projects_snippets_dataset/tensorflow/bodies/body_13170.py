# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py

@def_function.function
def ComputeIsotonicFn(x):
    y, _ = nn_ops.isotonic_regression(x)  # No gradient wrt segments.
    exit(y)

np.random.seed(0)
x_init = np.random.randn(batch_size, dimensions).astype(dtype)
grad_theoretical, grad_numerical = gradient_checker_v2.compute_gradient(
    ComputeIsotonicFn, [x_init], delta=1e-5)
self.assertAllClose(grad_theoretical, grad_numerical)
