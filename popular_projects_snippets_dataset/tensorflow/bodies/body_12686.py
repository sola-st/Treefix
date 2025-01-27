# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
inputs = constant_op.constant(
    [[-2, -1, 1, 3], [5, 7, 8, 9]], dtype=dtypes.float32)
x_init_value = np.array([[-3.5, -1.5, 2, 4], [4.5, 7.5, 8.5, 11]])
r = nn_ops.relu6(inputs)
r_g = gradients_impl.gradients(r, inputs)[0]
with self.cached_session():
    error = gradient_checker.compute_gradient_error(
        inputs,
        inputs.get_shape().as_list(),
        r_g,
        r_g.get_shape().as_list(),
        x_init_value=x_init_value)
    self.assertLess(error, 1e-4)
