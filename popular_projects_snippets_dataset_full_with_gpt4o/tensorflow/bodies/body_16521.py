# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py

if len(left_shape) > len(right_shape):
    output_shape = left_shape
else:
    output_shape = right_shape
l = np.random.randn(*left_shape)
r = np.random.randn(*right_shape)

with self.cached_session():
    left_tensor = constant_op.constant(l, shape=left_shape)
    right_tensor = constant_op.constant(r, shape=right_shape)
    output = math_ops.squared_difference(left_tensor, right_tensor)
    left_err = gradient_checker.compute_gradient_error(
        left_tensor, left_shape, output, output_shape, x_init_value=l)
    right_err = gradient_checker.compute_gradient_error(
        right_tensor, right_shape, output, output_shape, x_init_value=r)
self.assertLess(left_err, 1e-10)
self.assertLess(right_err, 1e-10)
