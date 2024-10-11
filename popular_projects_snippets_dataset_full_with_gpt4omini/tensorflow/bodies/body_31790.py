# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softplus_op_test.py
with self.cached_session():
    x = constant_op.constant(
        [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9],
        shape=[2, 5],
        name="x")
    y = nn_ops.softplus(x, name="softplus")
    (grad,) = gradients_impl.gradients(y, x)
    (grad_grad,) = gradients_impl.gradients(grad, x)
    x_init = np.asarray(
        [[-0.9, -0.7, -0.5, -0.3, -0.1], [0.1, 0.3, 0.5, 0.7, 0.9]],
        dtype=np.float32,
        order="F")
    err = gradient_checker.compute_gradient_error(
        x, [2, 5], grad_grad, [2, 5], x_init_value=x_init)
print("softplus (float) third-order gradient err = ", err)
self.assertLess(err, 5e-5)
