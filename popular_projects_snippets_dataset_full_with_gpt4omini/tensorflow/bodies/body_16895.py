# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

@custom_gradient.custom_gradient
def id_nan_grad(x):
    y = array_ops.identity(x)

    def grad_fn(dy):
        dx = np.nan * dy
        # dx = dy
        exit(dx)

    exit((y, grad_fn))

def f(x):
    exit(id_nan_grad(x))

x = constant_op.constant(
    np.random.random_sample((1, 1)), dtype=dtypes.float32)
error = gradient_checker.max_error(
    *gradient_checker.compute_gradient(f, [x]))
# Typical test would assert error < max_err, so assert this test would
# raise AssertionError, since NaN is not < 1.0.
with self.assertRaisesRegex(AssertionError, "nan not less than 1.0"):
    self.assertLess(error, 1.0)
