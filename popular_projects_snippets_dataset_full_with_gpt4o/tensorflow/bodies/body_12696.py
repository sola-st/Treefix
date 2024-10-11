# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
inputs = constant_op.constant(
    [[-2, -1, 1, 3], [5, 7, 8, 9]], dtype=dtypes.float32)
dummy = constant_op.constant(
    [[3, 1, -1, -2], [9, 8, 7, 6]], dtype=dtypes.float32)

elu = gen_nn_ops.elu(inputs)
elu_grad = gradients_impl.gradients(elu, inputs, grad_ys=dummy)[0]
with self.cached_session():
    error = gradient_checker.compute_gradient_error(
        inputs,
        inputs.shape,
        elu_grad,
        elu_grad.shape)
    self.assertLess(error, 1e-4)
